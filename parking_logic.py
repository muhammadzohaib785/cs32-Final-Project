import networkx as nx

def find_best_parking(user_node, destination_node, parking_lots, G, preference="walk"):
    """
    Finds the most suitable parking lot based on user preference.

    Parameters:
        user_node (int): The current node of the user.
        destination_node (int): The target destination node.
        parking_lots (dict): Dictionary of parking lot info keyed by node ID.
        G (networkx.Graph): The city graph.
        preference (str): "walk" or "drive".

    Returns:
        tuple or None: (node, name, drive_dist, walk_dist) or None if no available lot.
    """
    candidates = []

    for node, data in parking_lots.items():
        if data["parked"] < data["capacity"]:
            try:
                drive_dist = nx.shortest_path_length(G, source=user_node, target=node, weight='weight')
                walk_dist = nx.shortest_path_length(G, source=node, target=destination_node, weight='weight')
                candidates.append((node, data["name"], drive_dist, walk_dist))
            except nx.NetworkXNoPath:
                continue

    if not candidates:
        return None

    if preference == "walk":
        # Prefer minimal walking
        candidates.sort(key=lambda x: x[3])  # sort by walk_dist
    else:
        # Prefer minimal driving
        candidates.sort(key=lambda x: x[2])  # sort by drive_dist

    return candidates[0]
