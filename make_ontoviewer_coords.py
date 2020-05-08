import json
from cytoscape_utils import get_node_attr_from_cytoscape


nodes, edges = get_node_attr_from_cytoscape("edges_name.tsv.xgmml")

for node in nodes:
    if nodes[node]["name"] == "sac":
        nodes[node]["color"] = "orange"
        nodes[node]["type"] = "short_node"
    elif nodes[node]["name"] == "mc":
        nodes[node]["color"] = "green"
        nodes[node]["type"] = "short_node"
    else:
        if nodes[node]["name"] == "stuff accumulating cell":
            nodes[node]["color"] = "orange"
        elif nodes[node]["name"] == "motile cell":
            nodes[node]["color"] = "green"
        else:
            nodes[node]["color"] = "black"
        nodes[node]["type"] = "chart_node"


########## HEMAT ##########
hemat_x_dist = 220
hemat_cols = [0, hemat_x_dist * 1, hemat_x_dist * 2, hemat_x_dist * 3.2, hemat_x_dist * 4.3]

hemat_y_dist = 220
heamat_rows = [hemat_y_dist * 0, hemat_y_dist * 1, hemat_y_dist * 2,
               hemat_y_dist * 3, hemat_y_dist * 4, hemat_y_dist * 5,
               hemat_y_dist * 6]

for i in range(len(heamat_rows)):
    heamat_rows[i] = 1350 - heamat_rows[i]  # yshift

nodes_coord_hemat = {
    29796: {'name': 'hematopoietic\ncell', 'x': (hemat_cols[3] - hemat_cols[0]) / 2,
            'y': heamat_rows[0] + hemat_y_dist * 0.5},

    29795: {'name': 'blood\ncell', 'x': 0, 'y': heamat_rows[1]},
    29800: {'name': 'granulocyte', 'x': 0, 'y': heamat_rows[3]},

    29833: {'name': 'myeloid\ncell', 'x': hemat_cols[1], 'y': heamat_rows[1]},
    29801: {'name': 'myeloid\nleukocyte', 'x': hemat_cols[1], 'y': heamat_rows[2]},
    29828: {'name': 'monocyte', 'x': hemat_cols[2], 'y': heamat_rows[3]},
    29835: {'name': 'CD14-positive\nmonocyte', 'x': hemat_cols[2], 'y': heamat_rows[4]},
    29850: {'name': 'classical\nmonocyte', 'x': hemat_cols[2], 'y': heamat_rows[5]},

    29782: {'name': 'mc**', 'x': 480, 'y': 1230},
    29825: {'name': 'leukocyte', 'x': hemat_x_dist * 2, 'y': heamat_rows[1]},
    29827: {'name': 'nongranular\nleukocyte', 'x': hemat_cols[3], 'y': heamat_rows[2]},
    29824: {'name': 'dendritic\ncell', 'x': hemat_cols[2], 'y': heamat_rows[2]},

    29849: {'name': 'phagocyte', 'x': (hemat_cols[1] - hemat_cols[0]) / 2, 'y': (heamat_rows[4] + heamat_rows[5]) / 2},
    29781: {'name': 'mc**', 'x': hemat_cols[0], 'y': heamat_rows[4] + hemat_y_dist * .2},
    29778: {'name': 'sac*', 'x': hemat_cols[1], 'y': heamat_rows[4] + hemat_y_dist * .2},
    29843: {'name': 'hematopoietic\nprecursor\ncell', 'x': hemat_cols[3], 'y': heamat_rows[1]},

    29826: {'name': 'nucleate\ncell', 'x': hemat_cols[4], 'y': heamat_rows[2]},
    29799: {'name': 'lymphocyte', 'x': hemat_cols[4], 'y': heamat_rows[3]},
    29818: {'name': 'lymphocyte\nof B lineage', 'x': hemat_cols[3], 'y': heamat_rows[4]},
    29817: {'name': 'B cell', 'x': hemat_cols[3], 'y': heamat_rows[5]},
    29798: {'name': 'T cell', 'x': hemat_cols[4], 'y': heamat_rows[4]},
    29830: {'name': 'alpha-beta\nT cell', 'x': hemat_cols[4], 'y': heamat_rows[5]},
    29829: {'name': 'CD8-positive,\nalpha-beta\nT cell', 'x': hemat_cols[4], 'y': heamat_rows[6]}, }

########## EPITH ##########
first_row_y = 2160
nodes_coord_epith = {  # 1239

    29788: {'name': 'epithelial\ncell', 'x': (250 + 1900) / 2, 'y': 2600},

    29792: {'name': 'columnar-cuboidal\nepithelial\ncell', 'x': 250, 'y': first_row_y},
    29811: {'name': 'neurecto-epithelial\ncell', 'x': 250, 'y': 1866},
    29810: {'name': 'melanocyte', 'x': 250, 'y': 1661},
    54910: {'name': 'sac*', 'x': 0, 'y': 1934},
    29809: {'name': 'pigment\ncell', 'x': 0, 'y': 1725},

    29832: {'name': 'ecto-epithelial\ncell', 'x': 550, 'y': first_row_y},
    29838: {'name': 'general\necto-epithelial\ncell', 'x': 550, 'y': 1866},

    29790: {'name': 'squamous\nepithelial\ncell', 'x': 800, 'y': first_row_y},
    29793: {'name': 'mesothelial\ncell', 'x': 980, 'y': 1700},
    29789: {'name': 'blood\nvessel\nendothelial\ncell', 'x': 800, 'y': 1450},
    29794: {'name': 'lining\ncell', 'x': 1030, 'y': 1947},
    29805: {'name': 'meso-epithelial\ncell', 'x': 1250, 'y': first_row_y},
    29804: {'name': 'endothelial\ncell', 'x': 1250, 'y': 1800},
    29791: {'name': 'endothelial\ncell\nof vascular\ntree', 'x': 1250, 'y': 1500},

    29845: {'name': 'kidney\nepithelial\ncell', 'x': 1470, 'y': first_row_y},
    29844: {'name': 'epithelial\ncell of\nnephron', 'x': 1470, 'y': 1866},

    29848: {'name': 'hepatocyte', 'x': 1670, 'y': first_row_y},
    29797: {'name': 'epithelial\ncell\nof lung', 'x': 1025, 'y': first_row_y},

    29836: {'name': 'endo-epithelial\ncell', 'x': 1900, 'y': first_row_y},
    29775: {'name': 'respiratory\nepithelial\ncell', 'x': 1800, 'y': 1866},
    29776: {'name': 'epithelial\ncell of\nalimentary\ncanal', 'x': 2000, 'y': 1866},
}

########## CONNECT ##########
anchor_x, anchor_y = (1470, 1750)
x_dist, y_dist = (220, 220)
cols = [x_dist * 0, x_dist * 1, x_dist * 2, x_dist * 3, x_dist * 4]
cols = [anchor_x + c for c in cols]

rows = [y_dist * 0, y_dist * 1, y_dist * 2, y_dist * 3, y_dist * 4.2]
rows = [anchor_y - r for r in rows]

nodes_coord_connect = {
    29787: {'name': 'connective\ntissue\ncell', 'x': cols[2], 'y': rows[1]},

    29808: {'name': 'fat\ncell', 'x': cols[0], 'y': rows[2]},

    29786: {'name': 'fibroblast', 'x': cols[1], 'y': rows[2]},
    29842: {'name': 'skin\nfibroblast', 'x': cols[0], 'y': rows[3]},
    29840: {'name': 'preadipocyte', 'x': cols[1], 'y': rows[3]},

    29820: {'name': 'stromal\ncell', 'x': cols[2], 'y': rows[2]},
    29812: {'name': 'secretory\ncell', 'x': cols[3], 'y': rows[2]},
    29819: {'name': 'extracellular\nmatrix\nsecreting\ncell', 'x': cols[2], 'y': rows[3]},
    29847: {'name': 'GAG\nsecreting\ncell', 'x': cols[2], 'y': rows[4]},
    29784: {'name': 'stem\ncell', 'x': cols[4], 'y': rows[0]},
    29807: {'name': 'multi\nfate\nstem\ncell', 'x': cols[4], 'y': rows[1]},
    29806: {'name': 'mesenchymal\ncell', 'x': cols[4], 'y': rows[2]},
    29780: {'name': 'mc**', 'x': cols[3] + x_dist * .3, 'y': rows[1] - y_dist * .3},
    29777: {'name': 'sac*', 'x': cols[0], 'y': rows[1] - y_dist * .3},
}

########## MUSCLE ##########
anchor_x, anchor_y = (1400, 800)
x_dist, y_dist = (220, 220)

nodes_coord_muscle = {
    29815: {'name': 'electrically\nresponsive\ncell', 'x': anchor_x + x_dist * .5, 'y': anchor_y},
    29813: {'name': 'contractile\ncell', 'x': anchor_x - x_dist * .5, 'y': anchor_y},
    29814: {'name': 'muscle\ncell', 'x': anchor_x, 'y': anchor_y - y_dist * 1},
    29823: {'name': 'smooth\nmuscle\ncell', 'x': anchor_x, 'y': anchor_y - y_dist * 2},
    29822: {'name': 'vascular\nassociated\nsmooth\nmuscle\ncell', 'x': anchor_x, 'y': anchor_y - y_dist * 3.2},
}

########## MUSCLE ##########
anchor_x, anchor_y = (1700, 550)
x_dist, y_dist = (220, 220)

cols = [x_dist * 0, x_dist * 1, x_dist * 2, x_dist * 3]
cols = [anchor_x + c for c in cols]

rows = [y_dist * 0, y_dist * 1, y_dist * 2, y_dist * 3, y_dist * 4]
rows = [anchor_y - r for r in rows]

nodes_coord = {
    29803: {'name': 'neural\ncell', 'x': cols[0], 'y': rows[0]},
    29802: {'name': 'neuron\nassociated\ncell', 'x': cols[0], 'y': rows[1]},
    29846: {'name': 'glial\ncell', 'x': cols[0], 'y': rows[2]},
    29839: {'name': 'embryonic\ncell', 'x': cols[1], 'y': rows[0]},
    29821: {'name': 'extraembryonic\ncell', 'x': cols[1], 'y': rows[1]},
    29841: {'name': 'cardiocyte', 'x': cols[1], 'y': rows[2]},
    29785: {'name': 'non-terminally\ndifferentiated\ncell', 'x': cols[2], 'y': rows[0]},
    29831: {'name': 'supportive\ncell', 'x': cols[2], 'y': rows[1]},
    29816: {'name': 'cellof skeletal\nmuscle', 'x': cols[2], 'y': rows[2]},
    29834: {'name': 'bone\ncell', 'x': cols[3], 'y': rows[0]},
    29837: {'name': 'bone\nmarrow\ncell', 'x': cols[3], 'y': rows[1]},

}

########## LEGEND ##########
anchor_x, anchor_y = (0, 2600)
x_dist, y_dist = (220, 200)
nodes_coord_legend = {
    29779: {'name': '*stuff\naccumulating\ncell', 'x': anchor_x, 'y': anchor_y},
    29783: {'name': '**motile\ncell', 'x': anchor_x + x_dist, 'y': anchor_y},
}


nodes_coord.update(nodes_coord_epith)
nodes_coord.update(nodes_coord_hemat)
nodes_coord.update(nodes_coord_muscle)
nodes_coord.update(nodes_coord_connect)
nodes_coord.update(nodes_coord_legend)

for node_id in nodes_coord:
    nodes[str(node_id)]["node_print_name"] = nodes_coord[node_id]["name"]
    nodes[str(node_id)]["y"] = nodes_coord[node_id]["y"]
    nodes[str(node_id)]["x"] = nodes_coord[node_id]["x"]

ontoviewer_coords = {
    "nodes": nodes,
    "edges": edges
}

with open("ontoviewer_graph.json", "w") as file_handler:
    json.dump(ontoviewer_coords, file_handler, indent=4)

