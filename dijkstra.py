import sys

class Graph:

    def __init__(self): #initialize set of nodes, and dict of edges. 
        self.nodes = {'A','B','C','D','E','F'}
        self.edges = {
            'A': [('B', 11), ('C', 16)],
            'B': [('A', 11), ('C', 14), ('D', 18)],
            'C': [('A', 16), ('B', 14), ('D', 10), ('E', 17)],
            'D': [('B', 18), ('C', 10), ('E', 15), ('F', 12)],
            'E': [('C', 17), ('D', 15), ('F', 16)],
            'F': [('D', 12), ('E', 16)]
            }

    def djikstraAlgorithm(self, start_node, end_node):
        unvisited_dict = {node: sys.maxsize for node in self.nodes} #initializes dictionary containing nodes as keys and infinity
        unvisited_dict[start_node] = 0                              #as tentative distance value to each node, excluding start_node#
        visited_nodes = {}
        current_node = start_node

        while unvisited_dict: #loop while unvisited dictionary is not empty#
            min_node = min(unvisited_dict, key=unvisited_dict.get)

            if min_node == sys.maxsize: #if the minimum tentative distance is still infinity, break as there are no valid paths left#
                break

            current_node = min_node
            current_weight = unvisited_dict[current_node]
            del unvisited_dict[current_node]

            for neighbor, weight in self.edges[current_node]:

                if neighbor in visited_nodes:
                    continue
                
                tentative_distance = current_weight + weight
                if tentative_distance < unvisited_dict[neighbor]:
                    unvisited_dict[neighbor] = tentative_distance

            visited_nodes[current_node] = current_weight

        path = []

        if end_node in visited_nodes: #iterates backwards through shortest path and appends each node to the path list#
            while end_node != start_node:

                path.insert(0, end_node)

                for neighbor, weight in self.edges[end_node]:
                    if neighbor in visited_nodes and visited_nodes[end_node] - visited_nodes[neighbor] == weight:

                        end_node = neighbor
                        break
            
            path.insert(0, start_node)
            print(f"Nodes: {self.nodes}")
            print(f"Edges: {self.edges}")
            return path

g = Graph()

start_node = input("Enter start node: ").upper()
end_node = input("Enter end node: ").upper()

shortest_path = g.djikstraAlgorithm(start_node, end_node)

if shortest_path:
    print(f"Shortest path from {start_node} to {end_node}: {' -> '.join(shortest_path)}")

else:
    print(f"No path from {start_node} to {end_node} found.")
