"""
Implements Tarjan's algorithm for finding strongly connected components
in a graph.
https://en.wikipedia.org/wiki/Tarjan%27s_strongly_connected_components_algorithm
"""
# XXXX

from algorithms.graph import Tarjan
from algorithms.graph.graph import DirectedGraph


g1 = DirectedGraph(5)
g1.add_edge(1, 0)
g1.add_edge(0, 2)
g1.add_edge(2, 1)
g1.add_edge(0, 3)
g1.add_edge(3, 4)
print("SSC in first graph ")
#g1.SCC()

g2 = DirectedGraph(4)
g2.add_edge(0, 1)
g2.add_edge(1, 2)
g2.add_edge(2, 3)
print("nSSC in second graph ")
#g2.SCC()

g3 = DirectedGraph(7)
g3.add_edge(0, 1)
g3.add_edge(1, 2)
g3.add_edge(2, 0)
g3.add_edge(1, 3)
g3.add_edge(1, 4)
g3.add_edge(1, 6)
g3.add_edge(3, 5)
g3.add_edge(4, 5)
print("nSSC in third graph ")
#g3.SCC()

g4 = DirectedGraph(11)
g4.add_edge(0, 1)
g4.add_edge(0, 3)
g4.add_edge(1, 2)
g4.add_edge(1, 4)
g4.add_edge(2, 0)
g4.add_edge(2, 6)
g4.add_edge(3, 2)
g4.add_edge(4, 5)
g4.add_edge(4, 6)
g4.add_edge(5, 6)
g4.add_edge(5, 7)
g4.add_edge(5, 8)
g4.add_edge(5, 9)
g4.add_edge(6, 4)
g4.add_edge(7, 9)
g4.add_edge(8, 9)
g4.add_edge(9, 8)
print("nSSC in fourth graph ")
#g4.SCC();


g5 = DirectedGraph (5)
g5.add_edge(0, 1)
g5.add_edge(1, 2)
g5.add_edge(2, 3)
g5.add_edge(2, 4)
g5.add_edge(3, 0)
g5.add_edge(4, 2)
print("nSSC in fifth graph ")
#g5.SCC();