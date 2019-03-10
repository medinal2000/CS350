##########################################################
# Name: greedy_algorithms.py
# Description: contains implementation of Prim's algorithm
# Author: Medina Lamkin
# Last Edited: 13/03/19
##########################################################

import math
from graph import *

# doesn't account for graphs that have unconnected areas; does it need to?
# returns a minimum spanning tree and the minimun weight between the vertices
def prims_algorithm(graph):
    min_spanning_graph = Graph()
    total_weight = 0.0
    
    # get a starting key 
    for key in graph.graph:
        first_vertex = key
        break
    
    # add the first key to the min_spanning_graph
    min_spanning_graph.add_new_key(first_vertex)

    add_vertex = True

    # find the lowest weight which connects to an adjacent node
    while add_vertex: #(len(min_spanning_graph.graph) <= len(graph.graph))
        add_vertex = False
        #print("add_vertex: ", add_vertex)
        key1 = None  # when set, this key should already be in the min_spanning_graph
        key2 = None  # new key to add to the min spanning graph
        lowest_weight = math.inf
        #print("key1, key2: ", key1, key2)
        #print("lowest_weight", lowest_weight)
        
        for key in min_spanning_graph.graph:
             
            if key in graph.graph:
                for neighbour in graph.graph[key]:  
                    if neighbour[0] in min_spanning_graph.graph:
                        #print("neighbour: ", neighbour)
                        pass
                    else:
                        if neighbour[1] < lowest_weight:  # (neighbor node, edge weight)
                            lowest_weight = neighbour[1]
                            key1 = key
                            key2 = neighbour[0]  
                            add_vertex = True
                            #print("lowest_weight", lowest_weight)
                            #print("key1, key2: ", key1, key2)
            else:
                pass
        
        #if there is a neighboring vertex to the 
        if add_vertex:
            min_spanning_graph.add_new_key(key2)
            min_spanning_graph.add_edge(key1, key2, lowest_weight)
            total_weight += lowest_weight
            #print(min_spanning_graph.graph)
        
        #print("add_vertex: ", add_vertex)    
    return total_weight, min_spanning_graph
    
    