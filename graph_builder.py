import networkx as nx
size = 5
def build_city_graph(size):
    """
    Creates a 2D grid graph representing a simplified city.
    Each node is connected to its neighbors, forming a square grid.

    Parameters:
        size (int): The width/height of the grid. Default is 5 for a 5x5 grid.

    Returns:
        networkx.Graph: A graph with weighted edges (weight = 1).
    """
    G = nx.grid_2d_graph(size, size)
    G = nx.convert_node_labels_to_integers(G)
    for (u, v) in G.edges():
        G.edges[u, v]['weight'] = 1
    return G

