##########################################################
# Name: graph.py
# Description: contains implementation of graph class
# Author: Medina Lamkin
# Last Edited: 13/03/19
##########################################################

class Graph(object):
    
    # create an empty graph, which is a dictionary
    # each key has a list which contains tuples of 
    # adjacent nodes and corresponding weights
    def __init__(self):
        self.graph = {}
        
    # creates an 'empty' key with
    def add_new_key(self, key):
        self.graph[key] = []
        
    # assumes that the graph is directed; key1 will have an
    # edge to key2 of weight 'weight'
    # the keys should have been added to the graph before this
    def add_edge(self, key1, key2, weight):
        self.graph[key1].append((key2, weight))

    # prints the graph with 1 key per line
    def print_graph(self):
        print()
        for key in self.graph:
            print(key, ":", self.graph[key])
        print()

    # prints out the connected vertices and the weights
    # between them in the format vertex -- weight -- vertex
    def weight_between_vertices(self):
        print()
        for key in self.graph:
            for neighbour in self.graph[key]:
                print(key, "--", neighbour[1], "--", neighbour[0])
        print()
    
    # prints out the sum of all the weights
    def print_total_weight(self):
        total_weight = 0
        for key in self.graph:
            for neighbour in self.graph[key]:
                total_weight += neighbour[1]
                
        print("total_weight: ", total_weight)
        
