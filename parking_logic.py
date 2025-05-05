import networkx as nx


def get_walk_dist(candidate):
    return candidate[3]

def get_drive_dist(candidate):
    return candidate[2]

def find_best_parking(user_node, destination_node, parking_lots, G, preference="walk"):

    candidates = []

    for node, data in parking_lots.items():
        #check data from the dictionary of Parking lots if they are full
        #get the shortest path to get to a node using a function defined in the netwrorkx

        if data["parked"] < data["capacity"]:
            try:
                drive_dist = nx.shortest_path_length(G, source=user_node, target=node, weight='weight')
                walk_dist = nx.shortest_path_length(G, source=node, target=destination_node, weight='weight')
                candidates.append((node, data["name"], drive_dist, walk_dist))
            except nx.NetworkXNoPath:
                continue

    if not candidates:
        return None

    #Now based on the preferences,

    if preference == "walk":
        candidates.sort(key=get_walk_dist)
    else:
       candidates.sort(key=get_drive_dist)
       return candidates[0]
