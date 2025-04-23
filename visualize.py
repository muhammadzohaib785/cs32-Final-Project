import matplotlib.pyplot as plt
import networkx as nx


#This was made with the help of chatGPT to demonstrate how my code works

def show_city_map(G, parking_lots, user_node, destination_node):
    pos = nx.spring_layout(G, seed=1)

    # Decide color for each node
    colors = []
    labels = {}

    for node in G.nodes():
        if node == user_node:
            colors.append("blue")
            labels[node] = "User"
        elif node == destination_node:
            colors.append("yellow")
            labels[node] = "Dest"
        elif node in parking_lots:
            lot = parking_lots[node]
            if lot["parked"] < lot["capacity"]:
                colors.append("green")
            else:
                colors.append("red")
            labels[node] = lot["name"]
        else:
            colors.append("gray")

    # Draw the graph with custom labels
    nx.draw(G, pos, with_labels=True, labels=labels, node_color=colors, node_size=500)

    plt.title("City Map with Parking Lots")
    plt.savefig("city_map.png")
    print("Map saved as 'city_map.png'")
