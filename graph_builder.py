import networkx as nx
import random

RANDOM_EDGE_WEIGHTS = True

def build_balanced_city_graph(size):
    G = nx.grid_2d_graph(size, size)
    G = nx.convert_node_labels_to_integers(G)

    # Set horizontal weights
    for i in range(size):
        row_total = 10  # or any fixed total
        weights = [row_total // (size - 1)] * (size - 1)
        for j in range(size - 1):
            u = i * size + j
            v = u + 1
            G.edges[u, v]['weight'] = weights[j]

    # Set vertical weights
    for j in range(size):
        col_total = 10
        weights = [col_total // (size - 1)] * (size - 1)
        for i in range(size - 1):
            u = i * size + j
            v = u + size
            G.edges[u, v]['weight'] = weights[i]

    return G
