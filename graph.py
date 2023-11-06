import sys

class Graph:

    def __init__(self): #initialize set of nodes, and dict of edges. 
        self.nodes = set('A','B','C','D','E','F')
        self.edges = {
            'A': [('B', 11), ('C', 16)],
            'B': [('A', 11), ('C', 14), ('D', 18)],
            'C': [('A', 16), ('B', 14), ('D', 10), ('E', 17)],
            'D': [('B', 18), ('C', 10), ('E', 15), ('F', 12)],
            'E': [('C', 17), ('D', 15), ('F', 16)],
            'F': [('D', 12), ('E', 16)]
            }

    def djikstraAlgorithm(self, start_node, end_node):
        unvisited_dict = {node: sys.maxsize for node in self.nodes}
        unvisited_dict[start_node] = 0
        visited_nodes = {}
        current_node = start_node

        while unvisited_dict:
            min_node = min(unvisited_dict, key=unvisited_dict.get)

            if min_node == sys.maxsize:
                break

            current_node = min_node
            current_weight = unvisited_dict[current_node]
            del unvisited_dict[current_node]

            for neighbor, weight in self.edges[current_node]:

                if neighbor in visited_nodes:
                    continue
                
                tentative_distance