import networkx as nx
import heapq

def get_walk_dist(candidate):
    return candidate[3]

def get_drive_dist(candidate):
    return candidate[2]


def dijkstra(graph, start, target):
    """
    Just for reference, I had found this in the Networkx library
    that implemented Dijsktra but I chose to present Dijstkra here myself for
    the computational task requirement

    Function: nx.shortest_path_length()

    """
    distances = {node: float('inf') for node in graph.nodes}
    distances[start] = 0
    visited = set()
    heap = [(0, start)]

    while heap:
        curr_dist, curr_node = heapq.heappop(heap)

        if curr_node == target:
            return curr_dist  

        if curr_node in visited:
            continue

        visited.add(curr_node)

        for neighbor in graph.neighbors(curr_node):
            weight = graph.edges[curr_node, neighbor].get('weight', 1)
            new_dist = curr_dist + weight

            if new_dist < distances[neighbor]:
                distances[neighbor] = new_dist
                heapq.heappush(heap, (new_dist, neighbor))

    return float('inf')

def find_best_parking(user_node, destination_node, parking_lots, G, preference="walk"):

    candidates = []

    for node, data in parking_lots.items():
        if data["parked"] < data["capacity"]:
            try:
                drive_dist = dijkstra(G, user_node, node)
                walk_dist = dijkstra(G, node, destination_node)

                if drive_dist != float('inf') and walk_dist != float('inf'):
                    candidates.append((node, data["name"], drive_dist, walk_dist))
            except:
                continue

    if not candidates:
        return None

    if preference == "walk":
        candidates.sort(key=get_walk_dist)
    else:
        candidates.sort(key=get_drive_dist)

    return candidates[0]
