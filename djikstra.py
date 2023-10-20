import adjacency_matrix

class Dijkstra:
    
    
    def __init__(self):

        self.graph = adjacency_matrix.graph
        self.nodes = adjacency_matrix.nodes

        self.unvisited_nodes = []

        self.start = str('A')
        self.destination = str()

        self.current_node = self.start
        self.next_node = str()

        self.tentative_distance = {
            'A': 0,
            'B': 999,
            'C': 999,
            'D': 999,
            'E': 999,
            'F': 999
            }

        self.selectDestination()


    def selectDestination(self):
        
        print('Graph representation:')
        self.printGraphRepresentation()
        print()

        destination_found = False
        
        while destination_found == False:
            
            self.destination = str(input(f'\nYour start point is {self.start}. Enter destination: ').upper())

            if self.destination == self.start:
                print('\nDestination cannot be your start point. Pick again.')
                
            else:
                destination_found = True
        
        print(f'\nYou are travelling from {self.start} to {self.destination}.')
        self.markNodesUnvisited()
    
    
    def printGraphRepresentation(self):
        adjacency_matrix.print_graph()
        for i in self.graph:
            print(i)
        
        
    def markNodesUnvisited(self):

        for node in self.nodes:

            if node == self.start:
                pass

            else:
                self.unvisited_nodes.append(node)

        print(f'\nNodes {self.unvisited_nodes} are unvisited.')

        self.next_node = self.graph[0][1]
        self.algorithm(self.current_node, self.next_node)
                
    
    def algorithm(self, cur, v): 
        #for the current node, consider all of its unvisited neighbors.
        for neighbors in 


        
Dijkstra()
