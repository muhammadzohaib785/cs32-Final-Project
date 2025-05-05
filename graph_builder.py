import networkx as nx
import random


def build_random_city_graph(size, min_weight=1, max_weight=10):

    #Builds a size x size grid graph with random edge weights.
    #Each edge weight is an integer between min_weight and max_weight.
    
    G = nx.grid_2d_graph(size, size)
    G = nx.convert_node_labels_to_integers(G)

    for (u, v) in G.edges():
        G.edges[u, v]['weight'] = random.randint(min_weight, max_weight)

    return G
