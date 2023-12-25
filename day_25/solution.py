# Day 25, Merry Xmas! 🎅🎄

import random

from matplotlib import pyplot as plt
from networkx import Graph, draw, minimum_cut

DEBUG = False

graph = Graph()
nodes = []
with open(0) as f:
    for line in f.readlines():
        v = line.split(": ")[0]
        nodes.append(v)
        for w in line.split(": ")[1].strip().split(" "):
            if DEBUG:
                print(v, w)
            graph.add_edge(v, w, capacity=1)

# plot graph
if DEBUG:
    draw(graph, with_labels=True)
    plt.show()

cut_value = 0
partition = []
while cut_value != 3:
    v = random.choice(nodes)
    w = random.choice(nodes)
    cut_value, partition = minimum_cut(graph, v, w)
    if DEBUG:
        print(cut_value)
        print(partition)
        print(len(partition[0]) * len(partition[1]))

print("DAY 25:", len(partition[0]) * len(partition[1]))
