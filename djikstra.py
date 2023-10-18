import adjacency_matrix

class Djikstra:
    
    
    def __init__(self):
        self.graph = adjacency_matrix.graph
        self.unvisited_nodes = []
        self.destination = str()
        self.location = str('A')
        self.nodes = adjacency_matrix.vertices
        
        self.selectDestination()
        
        
    def markNodesUnvisited(self):
        for node in self.nodes:
            if node == self.location:
                pass
            else:
                self.unvisited_nodes.append(node)
                
    
    def tentativeDistance(self, node):
        if node == self.location:
            return int(0)
        else:
            return float(inf)
        
        
    def selectDestination(self):
        
        destination_found = False
        
        print('Graph representation:')
        self.printGraphRepresentation()
        print()
        
        while destination_found == False:
            
            self.destination = str(input(f'\nYour current location is {self.location}. Enter destination: ').upper())

            if self.destination == self.location:
                print('\nDestination cannot be your current location. Pick again.')
                
            else:
                destination_found = True
        
        print(f'\nYou are travelling from {self.location} to {self.destination}.')
        self.markNodesUnvisited()
    
    
    def printGraphRepresentation(self):
        adjacency_matrix.print_graph()
        for i in self.graph:
            print(i)
        
Djikstra()
