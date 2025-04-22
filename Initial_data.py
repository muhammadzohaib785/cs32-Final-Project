

import networkx as nx

import matplotlib.pyplot as plt



# Simulated city grid as a graph
G = nx.grid_2d_graph(5, 5)  # 5x5 grid (25 nodes)

# Relabel nodes to integers for clarity
G = nx.convert_node_labels_to_integers(G)

# Example: Add weights to edges (distance = 1 for all)
for (u, v) in G.edges():
    G.edges[u, v]['weight'] = 1


parking_lots = {
    2: {"name": "Lot A", "capacity": 10, "parked": 3},
    6: {"name": "Lot B", "capacity": 5, "parked": 5},  # full
    20: {"name": "Lot C", "capacity": 8, "parked": 4}
}



def find_best_parking(destination_node, parking_lots, G):
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


destination = 24  # Bottom right of the grid
result = find_best_parking(destination, parking_lots, G)

if result:
    print(f"Best lot: {result[1]} at node {result[0]} (distance {result[2]})")
else:
    print("No available parking lots found.")




def show_city_map(G, parking_lots, destination):
    pos = nx.spring_layout(G)
    colors = []

    for node in G.nodes():
        if node == destination:
            colors.append("blue")
        elif node in parking_lots and parking_lots[node]["parked"] < parking_lots[node]["capacity"]:
            colors.append("green")
        elif node in parking_lots:
            colors.append("red")
        else:
            colors.append("gray")

    nx.draw(G, pos, with_labels=True, node_color=colors, node_size=600)
    plt.show()


user_node = 0
destination_node = 24


best_lot = find_best_parking(destination_node, parking_lots, G)

if best_lot:
    print(f"Closest available parking lot to destination {destination_node}:")
    print(f"- Lot Name: {best_lot[1]}")
    print(f"- Located at node: {best_lot[0]}")
    print(f"- Distance to destination: {best_lot[2]} steps")
else:
    print("No available parking lots found.")




def show_city_map(G, parking_lots, user_node, destination_node):
    pos = nx.spring_layout(G, seed=42)  # Layout for consistent visuals
    colors = []

    for node in G.nodes():
        if node == user_node:
            colors.append("blue")
        elif node == destination_node:
            colors.append("yellow")
        elif node in parking_lots:
            lot = parking_lots[node]
            if lot["parked"] < lot["capacity"]:
                colors.append("green")
            else:
                colors.append("red")
        else:
            colors.append("gray")

    nx.draw(G, pos, with_labels=True, node_color=colors, node_size=600)
    labels = {node: parking_lots[node]["name"] for node in parking_lots}
    nx.draw_networkx_labels(G, pos, labels=labels, font_color="white")
    plt.title("Simulated City Map with Parking Lots")
    plt.savefig("city_map.png")
    print("Map saved as city_map.png")




show_city_map(G, parking_lots, user_node, destination_node)



