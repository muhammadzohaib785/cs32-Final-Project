import matplotlib.pyplot as plt
import networkx as nx

def show_city_map(G, parking_lots, user_node, destination_node, path=None, size=6):
    pos = {i * size + j: (j, -i) for i in range(size) for j in range(size)}  # grid layout
    colors = []
    labels = {}

    # Invert the destinations dictionary to look up names by node
    from destination_data import destinations
    destination_names_by_node = {v: k.capitalize() for k, v in destinations.items()}

    # Separate label dicts
    normal_labels = {}
    destination_labels = {}

    for node in G.nodes():
        if node == user_node:
            colors.append("blue")
            normal_labels[node] = f"User ({node})"
        elif node == destination_node:
            colors.append("yellow")
            destination_labels[node] = f"{destination_names_by_node.get(node, 'Dest')} ({node})"
        elif node in parking_lots:
            lot = parking_lots[node]
            colors.append("green" if lot["parked"] < lot["capacity"] else "red")
            normal_labels[node] = f"{lot['name']} ({node})"
        elif node in destination_names_by_node:
            colors.append("orange")
            destination_labels[node] = f"{destination_names_by_node[node]} ({node})"
        else:
            colors.append("gray")
            normal_labels[node] = str(node)

    # Draw nodes
    nx.draw_networkx_nodes(G, pos, node_color=colors, node_size=500)

    # Draw edges with weights as width
    weights = [G[u][v]['weight'] for u, v in G.edges()]
    nx.draw_networkx_edges(G, pos, width=[w for w in weights])

    # Draw path if available
    if path:
        edge_path = list(zip(path, path[1:]))
        nx.draw_networkx_edges(G, pos, edgelist=edge_path, edge_color="black", width=3)

    # Draw labels
    nx.draw_networkx_labels(G, pos, labels=normal_labels, font_size=8)

    # Offset destination labels only
    label_offset = -0.5
    dest_label_pos = {node: (x, y + label_offset) for node, (x, y) in pos.items() if node in destination_labels}
    nx.draw_networkx_labels(G, dest_label_pos, labels=destination_labels, font_size=8)

    plt.title("City Map with Parking Lots and Shortest Path")
    plt.savefig("city_map.png")
    print("Map saved as 'city_map.png'")
