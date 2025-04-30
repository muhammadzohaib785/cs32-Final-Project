import networkx as nx
import random

def random_partition(n, total):
    """Returns a list of n positive integers that sum to `total` with random values."""
    cuts = sorted(random.sample(range(1, total), n - 1))
    parts = [cuts[0]] + [cuts[i] - cuts[i - 1] for i in range(1, len(cuts))] + [total - cuts[-1]]
    return parts

def build_balanced_city_graph(size, row_total=10, col_total=10):
    G = nx.grid_2d_graph(size, size)
    G = nx.convert_node_labels_to_integers(G)

    edge_weights = {}

    # Horizontal edges: row-wise
    for i in range(size):
        weights = random_partition(size - 1, row_total)
        for j in range(size - 1):
            u = i * size + j
            v = u + 1
            edge_weights[(u, v)] = weights[j]

    # Vertical edges: column-wise
    for j in range(size):
        weights = random_partition(size - 1, col_total)
        for i in range(size - 1):
            u = i * size + j
            v = u + size
            edge_weights[(u, v)] = weights[i]

    # Assign weights to graph edges
    for (u, v) in G.edges():
        if (u, v) in edge_weights:
            G.edges[u, v]['weight'] = edge_weights[(u, v)]
        elif (v, u) in edge_weights:
            G.edges[u, v]['weight'] = edge_weights[(v, u)]
        else:
            G.edges[u, v]['weight'] = 1  # fallback (shouldn't happen)

    return G
