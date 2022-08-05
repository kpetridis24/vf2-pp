import random
import time

import networkx as nx
from inc.vf2pp import vf2pp_mapping

# Graph initialization
G1 = nx.gnp_random_graph(550, 0.55, 42)
G2 = nx.gnp_random_graph(550, 0.55, 42)

colors = [
    "white",
    "black",
    "green",
    "purple",
    "orange",
    "red",
    "blue",
    "pink",
    "yellow",
    "none",
]

# VF2++ initialization
for node in G1.nodes():
    color = colors[random.randrange(0, len(colors))]
    G1.nodes[node]["label"] = color
    G2.nodes[node]["label"] = color

G1_labels = nx.get_node_attributes(G1, "label")
G2_labels = nx.get_node_attributes(G2, "label")

# VF2++
t0 = time.time()
m = vf2pp_mapping(G1, G2, node_labels="label")
print(f"VF2++ elapsed time: {time.time() - t0}")

