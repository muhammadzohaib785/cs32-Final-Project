from graph_builder import build_city_graph
from parking_data import parking_lots
from parking_logic import find_best_parking
from visualize import show_city_map
from destination_data import destinations

G = build_city_graph(10)
user_node = 0

print("Available destinations:")
for name in destinations:
    print(f"- {name}")

destination_name = input("\nEnter your destination: ").strip().lower()

if destination_name not in destinations:
    print("Destination not recognized. Please try again.")
else:
    destination_node = destinations[destination_name]
    best_lot = find_best_parking(destination_node, parking_lots, G)

    if best_lot:
        print("\nBest parking lot found:")
        print(f"- Name: {best_lot[1]}")
        print(f"- Located at node: {best_lot[0]}")
        print(f"- Distance to destination: {best_lot[2]} steps")
    else:
        print("No available parking lots near your destination.")

    show_city_map(G, parking_lots, user_node, destination_node)
