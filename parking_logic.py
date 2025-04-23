import networkx as nx

def find_best_parking(destination_node, parking_lots, G):
    """
    Finds the closest available parking lot to the destination node.

    Parameters:
        destination_node (int): The node representing the user's destination.
        parking_lots (dict): Dictionary of parking lot info keyed by node ID.
        G (networkx.Graph): The city graph.

    Returns:
        tuple or None: (node, name, distance) of the best lot, or None if all are full.
    """
    best_lot = None
    best_distance = float("inf")

    for node, data in parking_lots.items():
        if data["parked"] < data["capacity"]:
            try:
                dist = nx.shortest_path_length(G, source=node, target=destination_node, weight='weight')
                if dist < best_distance:
                    best_distance = dist
                    best_lot = (node, data["name"], dist)
            except nx.NetworkXNoPath:
                continue  

    return best_lot
