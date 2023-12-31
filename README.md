# Dijkstra
Translating Dijkstra's algorithm for graph traversal into Python; part of CW1 for the Core Computing Concepts module.
## What is it?
Dijkstra’s algorithm is an algorithm created to find the shortest path between nodes within a weighted graph. The original algorithm would find the shortest path between two given nodes, but a more common variant is used that fixes a single node as the ‘source’ and finds the shortest paths to all other nodes in the graph, producing a shortest-path tree. The algorithm is commonly used for things like maps, where the weight of the edges represents distance. The algorithm runs in quadratic time complexity O(n^2), where n is the number of nodes.
## The Algorithm
1: Mark all nodes unvisited. Create a set of all the unvisited nodes called the unvisited set. 

2: Assign to every node a tentative distance value: set it to zero for the initial node and to infinity for all other nodes. During the run of the algorithm, the tentative distance of a node v is the length of the shortest path discovered so far between the node v and the starting node. Since initially no path is known to any other node than the source itself (which is a path of length 0), all other tentative distances are initially set to infinity. Set the initial node as current. 

3: For the current node, consider all of its unvisited neighbors and calculate their tentative distances through the current node. Compare the newly calculated tentative distance to the one currently assigned to the neighbor and assign it the smaller one.  

4: When done considering all unvisited neighbors of the current node, make the current node as visited and remove it from the unvisited set. A visited node will never be checked again. 

5: If the destination node has been marked visited (for a path going from node A to node B), stop. The algorithm has finished. 

6: Otherwise, select the unvisited node that is marked with the smallest tentative distance, set it as the new current node, and go back to step 3. 

## Graph Structure
The sample graph structure used in the program is composed of 6 nodes marked A-F, and 9 nodes:
    
    A - B    11
    
    A - C    16
    
    B - C    14
    
    B - D    18
    
    C - D    10
    
    C - E    17
    
    D - E    15
    
    D - F    12

    E - F    16

## Graph Visualisation

![image](https://github.com/pauchxk/Djikstra/assets/58793330/62f1a511-449f-4d4f-b99b-2878d9b54c32)

## Sources
https://www.bogotobogo.com/python/python_graph_data_structures.php

https://www.python.org/doc/essays/graphs/

https://docs.python.org/3/tutorial/classes.html

https://www.educative.io/answers/how-to-implement-a-graph-in-python
