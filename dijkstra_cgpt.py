#NOTE: learn how this program works inside out, and rewrite it yourself. 
#don't give up on this project. use what you learn here and rework your attempt.

import sys

class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = {}

    def add_node(self, value):
        self.nodes.add(value)
        if value not in self.edges:
            self.edges[value] = []

    def add_edge(self, from_node, to_node, weight):
        self.edges[from_node].append((to_node, weight))
        self.edges[to_node].append((from_node, weight))

    def dijkstra(self, start_node, end_node):
        unvisited = {node: sys.maxsize for node in self.nodes}
        unvisited[start_node] = 0
        visited = {}
        current_node = start_node

        while unvisited:
            min_node = min(unvisited, key=unvisited.get)
            print(f'min node {min_node}.')

            if unvisited[min_node] == sys.maxsize:
                break

            current_node = min_node
            current_weight = unvisited[current_node]
            print(f'current weight {current_weight}.')
            del unvisited[current_node]

            for neighbor, weight in self.edges[current_node]:
                if neighbor in visited:
                    continue

                tentative_distance = current_weight + weight
                if tentative_distance < unvisited[neighbor]:
                    unvisited[neighbor] = tentative_distance

            visited[current_node] = current_weight

        path = []
        if end_node in visited:
            while end_node != start_node:
                path.insert(0, end_node)
                for neighbor, weight in self.edges[end_node]:
                    if neighbor in visited and visited[end_node] - visited[neighbor] == weight:
                        end_node = neighbor
                        break

            path.insert(0, start_node)

        return path

# Example usage
g = Graph()
g.add_node("A")
g.add_node("B")
g.add_node("C")
g.add_node("D")
g.add_node("E")
g.add_node('F')

g.add_edge('A', 'B', 11)
g.add_edge('A', 'C', 16)
g.add_edge('B', 'C', 14)
g.add_edge('B', 'D', 18)
g.add_edge('C', 'D', 10)
g.add_edge('C', 'E', 17)
g.add_edge('D', 'E', 15)
g.add_edge('D', 'F', 12)
g.add_edge('E', 'F', 16)

start_node = "A"
end_node = "F"

shortest_path = g.dijkstra(start_node, end_node)
if shortest_path:
    print(f"Shortest path from {start_node} to {end_node}: {' -> '.join(shortest_path)}")
else:
    print(f"No path from {start_node} to {end_node} found.")

#CHAT-GPT's explanation:
# Graph Class:

# The program begins by defining a Graph class. This class is used to create and manipulate a weighted graph.

# python
# Copy code
# class Graph:
#     def __init__(self):
#         self.nodes = set()
#         self.edges = {}
# The nodes attribute stores the set of all nodes in the graph.
# The edges attribute is a dictionary where each key is a node, and its corresponding value is a list of tuples, each representing an edge to a neighboring node and its weight.
# add_node Method:

# The add_node method allows you to add nodes to the graph. It also initializes an empty list of edges for each new node.

# python
# Copy code
# def add_node(self, value):
#     self.nodes.add(value)
#     if value not in self.edges:
#         self.edges[value] = []
# add_edge Method:

# The add_edge method allows you to add edges with associated weights to the graph. It appends a tuple representing the neighboring node and the weight to the list of edges for both nodes connected by the edge.

# python
# Copy code
# def add_edge(self, from_node, to_node, weight):
#     self.edges[from_node].append((to_node, weight))
#     self.edges[to_node].append((from_node, weight))
# Dijkstra's Algorithm:

# The heart of the program is the dijkstra method, which implements Dijkstra's algorithm for finding the shortest path between two nodes in the graph. Here's the step-by-step breakdown of the algorithm:

# It initializes the unvisited dictionary, which stores the tentative distances to each node. It sets the distance of the start_node to 0 and all other nodes to infinity (sys.maxsize).
# python
# Copy code
# def dijkstra(self, start_node, end_node):
#     unvisited = {node: sys.maxsize for node in self.nodes}
#     unvisited[start_node] = 0
#     visited = {}
#     current_node = start_node
# It enters a loop where it selects the node with the smallest tentative distance (min_node) from the unvisited dictionary.

# If the smallest tentative distance is still sys.maxsize, it means there are no valid paths left, and the loop breaks.

# It considers all unvisited neighbors of the current node, calculates their tentative distances, and updates them if a shorter path is found.

# It marks the current node as visited and removes it from the unvisited dictionary.

# If the end_node is marked as visited, it breaks out of the loop since the shortest path has been found.

# The code then constructs the shortest path by backtracking from the end_node to the start_node, following the nodes with the smallest distances.

# Example Usage:

# The program concludes with an example usage of the Graph class. It creates a sample graph with nodes A, B, C, D, E, and F and defines edges with weights between them.

# Finding and Printing the Shortest Path:

# It specifies a start_node and end_node, then calls the dijkstra method to find the shortest path between these nodes.

# If a valid path is found (i.e., the shortest_path is not empty), it prints the path and its associated weights.

# If there is no path between the start_node and end_node, it prints a message indicating that no path was found.

# The program is a Python implementation of Dijkstra's algorithm for weighted graph traversal using object-oriented programming, and it can be applied to various scenarios where you need to find the shortest path in a weighted graph.