"""
Bipartite graph is a graph whose vertices can be divided into two disjoint and independent sets.
(https://en.wikipedia.org/wiki/Bipartite_graph)
Time complexity is O(|E|)
Space complexity is O(|V|)
이분법

"""
from algorithms.graph import check_bipartite
graph = [[0, 1, 0, 1],
           [1, 0, 1, 0],
           [0, 1, 0, 1],
           [1, 0, 1, 0]]

print(check_bipartite(graph))