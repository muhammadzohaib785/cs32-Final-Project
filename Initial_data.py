# main.py

# Sample parking lot data
parking_lots = [
    {"id": 0, "name": "Lot A", "x": 2, "y": 3, "capacity": 50, "parked": 20},
    {"id": 1, "name": "Lot B", "x": 5, "y": 7, "capacity": 30, "parked": 25},
    {"id": 2, "name": "Lot C", "x": 1, "y": 1, "capacity": 20, "parked": 15},
    {"id": 3, "name": "Lot D", "x": 8, "y": 2, "capacity": 40, "parked": 40},
    {"id": 4, "name": "Lot E", "x": 4, "y": 5, "capacity": 25, "parked": 10}
]

# Sample user location
user_x, user_y = 3, 4

# Find the closest lot with space
def distance(x1, y1, x2, y2):
    return ((x1 - x2)**2 + (y1 - y2)**2)**0.5

available_lots = [lot for lot in parking_lots if lot["parked"] < lot["capacity"]]
closest_lot = min(available_lots, key=lambda lot: distance(user_x, user_y, lot["x"], lot["y"]))

print(f"Closest available lot: {closest_lot['name']}")
