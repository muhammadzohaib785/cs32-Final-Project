import matplotlib.pyplot as plt
import networkx as nx


#This was made with the help of chatGPT to demonstrate how my code works
def show_city_map(G, parking_lots, user_node, destination_node, path=None):
    pos = nx.kamada_kawai_layout(G, weight='weight')
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
            colors.append("green" if lot["parked"] < lot["capacity"] else "red")
            labels[node] = lot["name"]
        else:
            colors.append("gray")

    nx.draw(G, pos, node_color=colors, labels=labels, with_labels=True, node_size=500)

    # Draw edges normally
    weights = [G[u][v]['weight'] for u, v in G.edges()]
    nx.draw_networkx_edges(G, pos, width=[w for w in weights])

    # Highlight the shortest path
    if path:
        edge_path = list(zip(path, path[1:]))
        nx.draw_networkx_edges(G, pos, edgelist=edge_path, edge_color="black", width=3)

    plt.title("City Map with Parking Lots and Shortest Path")
    plt.savefig("city_map.png")
    print("Map saved as 'city_map.png'")



