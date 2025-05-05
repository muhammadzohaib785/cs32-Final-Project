import networkx as nx
import random


#GPT Helped build the Map
def random_partition(n, total):
    """
    Returns a list of `n` positive integers that sum to `total`,
    where each part is randomly determined.
    """

    # Step 1: Choose n - 1 random cut points between 1 and total - 1
    cut_points = random.sample(range(1, total), n - 1)

    # Step 2: Sort the cut points to create meaningful partitions
    cut_points.sort()

    # Step 3: Initialize the list to store the partitioned values
    parts = []

    # Step 4: The first part is from 0 to the first cut point
    parts.append(cut_points[0])

    # Step 5: The middle parts are differences between consecutive cut points
    for i in range(1, len(cut_points)):
        parts.append(cut_points[i] - cut_points[i - 1])

    # Step 6: The last part is from the last cut point to the total
    parts.append(total - cut_points[-1])

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
