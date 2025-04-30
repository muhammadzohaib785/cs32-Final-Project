from graph_builder import build_city_graph
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

if destination_name not in destinations:
    print("Destination not recognized. Please try again.")
    exit()

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

# Find best parking lot near the user
best_lot = find_best_parking(user_node, parking_lots, G)

# Show best parking lot
if best_lot:
    print("\nBest parking lot found:")
    print(f"- Name: {best_lot[1]}")
    print(f"- Located at node: {best_lot[0]}")
    print(f"- Distance from you: {best_lot[2]} steps")
else:
    print("No available parking lots near your location.")

# Get shortest path to destination
try:
    path = nx.shortest_path(G, source=user_node, target=destination_node, weight='weight')
    print("\nShortest path to your destination:")
    print(" -> ".join(map(str, path)))
except nx.NetworkXNoPath:
    path = None
    print("No path found from your location to the destination.")

# Visualize map
show_city_map(G, parking_lots, user_node, destination_node, path)

# Print edge weights
print("\nEdge Weights:")
for u, v, data in G.edges(data=True):
    print(f"Edge ({u}, {v}) has weight {data['weight']}")
