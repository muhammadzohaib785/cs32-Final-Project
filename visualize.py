import matplotlib.pyplot as plt
import networkx as nx

#I significantly used chat gpt for this code:

def show_city_map(G, parking_lots, user_node, destination_node, path=None, size=6):
    pos = {i * size + j: (j, -i) for i in range(size) for j in range(size)}  # grid layout
    colors = []

    from destination_data import destinations
    destination_names_by_node = {v: k.capitalize() for k, v in destinations.items()}

    # Separate label dicts and style dicts
    normal_labels = {}
    destination_labels = {}
    whitebox_labels = {}  # nodes whose labels should have a white background
    

    for node in G.nodes():
        if node == user_node:
            colors.append("blue")
            label = f"User ({node})"
            normal_labels[node] = label
            whitebox_labels[node] = label

        elif node == destination_node:
            colors.append("yellow")
            label = f"{destination_names_by_node.get(node, 'Dest')} ({node})"
            destination_labels[node] = label
            whitebox_labels[node] = label

        elif node in parking_lots:
            lot = parking_lots[node]
            colors.append("green" if lot["parked"] < lot["capacity"] else "red")
            label = f"{lot['name']} ({node})"
            normal_labels[node] = label
            whitebox_labels[node] = label

        elif node in destination_names_by_node:
            colors.append("orange")
            label = f"{destination_names_by_node[node]} ({node})"
            destination_labels[node] = label
            whitebox_labels[node] = label

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

    # Draw regular labels (centered, no background)
    plain_labels = {node: lbl for node, lbl in normal_labels.items() if node not in whitebox_labels}
    nx.draw_networkx_labels(G, pos, labels=plain_labels, font_size=8)

    # Offset destination labels
    label_offset = -0.5
    dest_label_pos = {node: (x, y + label_offset) for node, (x, y) in pos.items() if node in destination_labels}
    nx.draw_networkx_labels(G, dest_label_pos, labels=destination_labels, font_size=8,
                            bbox=dict(facecolor='white', edgecolor='none', pad=1))

    # Draw whitebox labels (user and parking lots) — centered
    non_destination_whitebox_labels = {
    node: label for node, label in whitebox_labels.items() if node not in destination_labels
    }
    non_destination_whitebox_pos = {node: pos[node] for node in non_destination_whitebox_labels}
    nx.draw_networkx_labels(G, non_destination_whitebox_pos, labels=non_destination_whitebox_labels,
                        font_size=8, bbox=dict(facecolor='white', edgecolor='none', pad=1))

    plt.title("City Map with Parking Lots and Shortest Path")
    plt.savefig("city_map.png")
    print("Map saved as 'city_map.png'")
