class Djikstra:
    #12/10/23: need to create the graph structure. need a list of nodes, and a dictionary of edges and their weights.
    def __init__(self):
        
        self.graph = ['A','B','C','D','E','F']
        
        self.edges = {['A','B'],11,
                      ['A','C'],16,
                      ['B','C'],14,
                      ['B','D'],18,
                      ['C','D'],10,
                      ['C','E'],17,
                      ['D','E'],15,
                      ['D','F'],12,
                      ['E','F'],16}
        
        self.unvisited_nodes = []
