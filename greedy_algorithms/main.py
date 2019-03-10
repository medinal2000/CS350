##########################################################
# Name: main.py
# Description: runs the greedy algorithms
# Author: Medina Lamkin
# Last Edited: 13/03/19
##########################################################

from graph import *
from greedy_algorithms import * 

try:
    file = open(r"C:\Users\medin\Desktop\city_pairs.txt")
#    file = open(r"C:\Users\medin\Desktop\test.txt")

except IOError:
    print("File not found or path is incorrect")
    exit()
    
# create a graph object to store vertices and edges
graph = Graph()

# save vertices and edges
for line in file:
    data = line.split()
    key1 = data[0]
    key2 = data[1]
    weight = float(data[2]) 
    
    if key1 in graph.graph:
        graph.add_edge(key1, key2, weight)
    else:
        graph.add_new_key(key1)
        graph.add_edge(key1, key2, weight)
        
        
graph.print_graph()

# create the minimal spanning tree
min_distance, min_spanning_graph = prims_algorithm(graph)

min_spanning_graph.print_graph()
min_spanning_graph.weight_between_vertices()
min_spanning_graph.print_total_weight()


print("min dist: ", min_distance)

file.close()