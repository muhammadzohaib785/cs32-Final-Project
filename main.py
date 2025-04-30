from graph_builder import build_balanced_city_graph
from parking_data import parking_lots
from parking_logic import find_best_parking
from visualize import show_city_map
from destination_data import destinations
import networkx as nx

# Set size of city
SIZE = 6
G = build_balanced_city_graph(SIZE)

# Show available destinations
print("Available destinations:")
for name in destinations:
    print(f"- {name}")

# Get destination
destination_name = input("\nEnter your destination: ").strip().lower()

while destination_name not in destinations:
    print("Destination not recognized. Please try again.")
    destination_name = input("\nEnter your destination: ").strip().lower()
    continue

destination_node = destinations[destination_name]

# Get user location
try:
    user_node = int(input("Enter your current location (node number): "))
except ValueError:
    print("Invalid input. Please enter an integer.")
    exit()

if user_node not in G.nodes():
    print("Invalid start node. Not in graph.")
    exit()

# Exclude current location if it's a parking lot
if user_node in parking_lots:
    print("\nYou are currently at a parking lot. Searching for the next closest one...")
    adjusted_parking_lots = {node: lot for node, lot in parking_lots.items() if node != user_node}
else:
    adjusted_parking_lots = parking_lots

# Find best parking lot near the user
best_lot = find_best_parking(user_node, adjusted_parking_lots, G)

# Show best parking lot
if best_lot:
    print("\nBest parking lot found:")
    print(f"- Name: {best_lot[1]}")
    print(f"- Located at node: {best_lot[0]}")
    print(f"- Distance from you: {best_lot[2]} steps")
else:
    print("No available parking lots near your location.")

# Compute driving and walking paths
if best_lot:
    parking_node = best_lot[0]
    try:
        drive_path = nx.shortest_path(G, source=user_node, target=parking_node, weight='weight')
        walk_path = nx.shortest_path(G, source=parking_node, target=destination_node, weight='weight')
        full_path = drive_path[:-1] + walk_path  # avoid repeating the parking node

        print("\nDirections:")
        print("🚗 Drive to Parking Lot:")
        print(" -> ".join(map(str, drive_path)))
        print("🚶 Walk from Parking Lot to Destination:")
        print(" -> ".join(map(str, walk_path)))
    except nx.NetworkXNoPath:
        full_path = None
        print("No path found from your location to the destination.")
else:
    full_path = None

# Visualize map
show_city_map(G, parking_lots, user_node, destination_node, full_path, size=SIZE)

# Print edge weights
print("\nEdge Weights:")
for u, v, data in G.edges(data=True):
    print(f"Edge ({u}, {v}) has weight {data['weight']}")
