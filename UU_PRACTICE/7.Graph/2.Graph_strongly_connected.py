from algorithms.graph.check_digraph_strongly_connected import Graph

g1 = Graph(5)
g1.add_edge(0, 1)
g1.add_edge(1, 2)
g1.add_edge(2, 3)
g1.add_edge(3, 0)
g1.add_edge(2, 4)
g1.add_edge(4, 2)
print ("Yes") if g1.is_sc() else print("No")

g2 = Graph(4)
g2.add_edge(0, 1)
g2.add_edge(1, 2)
g2.add_edge(2, 3)
print ("Yes") if g2.is_sc() else print("No")
