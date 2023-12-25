import networkx as nx
import matplotlib.pyplot as plt

INPUT_FILE = r"advent of code\2023\day 25\input.txt"

with open(INPUT_FILE) as f:
    data = f.read().strip().split("\n")

graph = nx.Graph()
for line in data:
    component, connections = line.split(": ")
    for connection in connections.strip().split(" "):
        graph.add_edge(component, connection)


# options = {"with_labels": True}
# nx.draw(graph, **options)
# plt.show()

graph.remove_edges_from(nx.minimum_edge_cut(graph))
cluster1, cluster2 = list(nx.connected_components(graph))

ans = len(cluster1) * len(cluster2)
print(f"Part 1: {ans}")
