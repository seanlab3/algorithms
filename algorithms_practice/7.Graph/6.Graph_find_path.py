
from algorithms.graph.find_path import find_all_path,find_shortest_path

myGraph = {'A': ['B', 'C'],
           'B': ['C', 'D'],
           'C': ['D', 'F'],
           'D': ['C'],
           'E': ['F'],
           'F': ['C']}
print(find_all_path(myGraph, 'A', 'F'))
print("=============================")
print(find_shortest_path(myGraph, 'A', 'D'))