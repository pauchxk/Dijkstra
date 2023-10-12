class Djikstra:
    #12/10/23: need to create the graph structure. need a list of nodes, and a dictionary of edges and their weights.
    def __init__(self):
        
        self.graph = ['A','B','C','D','E','F']
        
        self.edges = {['A','B'],7,
                      ['A','C'],9,
                      ['B','C'],14,
                      ['B','D'],2,
                      ['C','D'],10,
                      ['C','F'],13,
                      ['D','E'],5,
                      ['D','F'],6,
                      ['E','F'],16}
        
        self.unvisited_nodes = []