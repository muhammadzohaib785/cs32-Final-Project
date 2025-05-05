# cs32-Final-Project

Description:
This project is a Python-based smart parking assistant that simulates a city grid to help users find the nearest available parking spot to a given destination. The city is represented as a 2D grid graph using NetworkX, where intersections are nodes and roads are weighted edges reflecting distance or travel time. Parking lots are placed at selected nodes and marked as available or full based on simulated real-time data. When the user selects a destination, the system calculates the shortest path to all available parking lots using Dijkstra’s algorithm and chooses the best one based on proximity and availability. A Matplotlib-based visualization then displays the city layout, the destination, all parking lots, edge weights, and the optimal path from the chosen lot to the destination. This simulation demonstrates how graph theory and algorithmic decision-making can be applied to real-world challenges in urban mobility and smart parking systems.

Citations:

1) NetwrokX (website) is the main source of all the functions used for this specific API and this was my main source for getting all the functions, their parameters information and for the basic understanding of how the functions run.

Link to Website: API DocumentationNetworkXhttps://networkx.org › documentation › networkx-0

2) Chat GPT: Helped me make the code for the file Visualise since it was beyond the skillsets required in this class. It also helped me build the data including the parking lot data, nodes, and gave me sample destinations in the map. Finally, I used GPT to help construct the map; while I coded the part to assign random weights to the edges myself, GPT helped using the functions from the Networkx library that I was not fully familiar with.
