import json
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
import numpy as np
import pandas as pd

# plt.style.use('helv_math')

PAD = 0


def custom_node_bottom(node, t_display, chart_width_display, height_display, ax, fig):
    # display coord of text + bbox
    graph_w_display, graph_h_display = (chart_width_display, height_display)
    graph_w_fig, graph_h_fig = fig.transFigure.inverted().transform((graph_w_display, graph_h_display))
    graph_x_display = t_display["p0x"] + (t_display["w"] - chart_width_display) / 2
    graph_y_display = t_display["p0y"] - height_display
    graph_x1_display, graph_y1_display = (graph_x_display + chart_width_display, t_display["p0y"])

    graph_x_fig, graph_y_fig = fig.transFigure.inverted().transform((graph_x_display, graph_y_display))

    ax1 = fig.add_axes([graph_x_fig, graph_y_fig, graph_w_fig, graph_h_fig])
    up, down, other = (node["up"], node["down"], node["other"])
    # count_sum = up + down + other
    # up = up / count_sum
    # down = down / count_sum
    # other = other / count_sum

    # ax1.barh([1], [up], color="#fb9a99", edgecolor="whitesmoke")
    # ax1.barh([1], [down], left=[up], color="#a6cee3", edgecolor="whitesmoke")
    # ax1.barh([1], [other], left=[up + down], color="lightgray", edgecolor="whitesmoke")
    ax1.set_xlim(-0.05, 1.05)
    ax1.set_ylim(0.45, 1.55)
    ax1.set_yticks([])
    ax1.set_xticks([])
    # ax1.axis("off")

    # draw major patch combining text and graph
    major_x_data, major_y_data = ax.transData.inverted().transform(
        (min(t_display["p0x"], graph_x_display), t_display["p0y"] - height_display))
    major_x1_data, major_y1_data = ax.transData.inverted().transform(
        (max(t_display["p1x"], graph_x1_display), t_display["p1y"]))
    major_w_data = major_x1_data - major_x_data
    major_h_data = major_y1_data - major_y_data

    rect = FancyBboxPatch((major_x_data - 1, major_y_data - 1), major_w_data + 2, major_h_data + 2, linewidth=1,
                          edgecolor=node["color"], facecolor='none', boxstyle="round,pad=10")
    p = ax.add_patch(rect)

    return p


def add_up_down_count_to_nodes(nodes, up_down_df):
    """Add up, down and other counts to each nodes.
    Modify `nodes` in-place"""

    columns = ["up", "down", "other"]

    for node in nodes.values():
        if not node["type"] == "chart_node":
            continue

        node_name = node["name"]
        if node_name in up_down_df.index:
            values = up_down_df.loc[node_name, columns]
            values = values / values.sum()
            values = values.tolist()
        else:
            values = (0., 0., 1.)

        for tag, val in zip(columns, values):
            nodes[node["id"]][tag] = val


def main(graph_filename, up_down_filename):

    with open(graph_filename) as fh:
        graph = json.load(fh)
        nodes, edges = (graph["nodes"], graph["edges"])

    up_down_df = pd.read_csv(up_down_filename, sep="\t", index_col=0)
    add_up_down_count_to_nodes(nodes, up_down_df)

    fig, ax = plt.subplots(figsize=(35, 25))

    ax.set_ylim(-100, 2700)
    ax.set_xlim(-150, 2500)

    node_to_text_display = {}
    node_to_text = {}
    node_to_patch = {}
    node_to_patch_center = {}

    for node_id, node in nodes.items():
        if node["type"] == "chart_node":
            t = ax.text(node["x"], node["y"], node["node_print_name"],
                        ha="center", va="center", fontsize=16)  # , bbox=bbox)

            renderer = fig.canvas.get_renderer()

            # get display coord of the text (bbox not included)
            # so we manually add PAD
            bbox_text = t.get_window_extent(renderer=renderer)
            t_display = {
                "w": bbox_text.width + PAD * 2,
                "h": bbox_text.height + PAD * 2,
                "p0x": bbox_text.p0[0] - PAD,
                "p0y": bbox_text.p0[1] - PAD,
                "p1x": bbox_text.p1[0] + PAD,
                "p1y": bbox_text.p1[1] + PAD, }

            node_to_text_display[node_id] = t_display
            node_to_text[node_id] = t

    wideleast_node = min([node_to_text_display[node["id"]] for node in nodes.values() if node["type"] == "chart_node"],
                         key=lambda x: x["w"])
    wideleast_display = wideleast_node["w"]

    mean_height_display = np.mean(
        [node_to_text_display[node["id"]]["h"] for node in nodes.values() if node["type"] == "chart_node"]) * .7

    for node_id, node in nodes.items():
        if node["type"] == "chart_node":
            p = custom_node_bottom(node, node_to_text_display[node_id], wideleast_display + 40,
                                   mean_height_display, ax, fig)
            node_to_patch[node_id] = p

            node_to_patch_center[node_id] = {
                "x": p.get_x() + p.get_width() / 2,
                "y": p.get_y() + p.get_height() / 2}
        else:
            node_to_patch_center[node_id] = {"x": node["x"], "y": node["y"]}
            bbox = dict(facecolor='none', edgecolor=node["color"], alpha=0.5, boxstyle="round,pad=.9")
            t = ax.text(node["x"], node["y"], node["name"], ha="center", va="center", fontsize=15, bbox=bbox)
            node_to_patch[node_id] = t

    for edge_id, edge in edges.items():
        v, u = (edge["source"], edge["target"])
        pos_u, pos_v = (node_to_patch_center[u], node_to_patch_center[v])
        arrow_coord = (pos_u["x"], pos_u["y"], pos_v["x"], pos_v["y"])
        ux, uy, vx, vy = arrow_coord
        ax.annotate("", (vx, vy), xytext=(ux, uy), arrowprops=dict(
            facecolor='black', patchA=node_to_patch[u], patchB=node_to_patch[v],
            shrinkA=.1, shrinkB=20, lw=.01, ec="black", headwidth=5, headlength=6, width=1))
    ax.axis("off")
    plt.show()
# fig.savefig("cl_spi1_newline.pdf", bbox_inches='tight')
# fig.savefig("cl_spi1_newline.png", bbox_inches='tight')
# fig.savefig("cl_spi1_newline.svg", bbox_inches='tight')


if __name__ == "__main__":
    main("ontoviewer_graph.json", "./25_pyRRF_500_new_onto_SPI1.new.tsv")
