# takes dict of sets
# each key is a vertex
# value is set of all edges connected to vertex
# returns list of lists (each sub list is a maximal clique)
# implementation of the basic algorithm described in:
# Bron, Coen; Kerbosch, Joep (1973), "Algorithm 457: finding all cliques of an undirected graph",

# XXXXXXXXX

from algorithms.graph import find_all_cliques



print(find_all_cliques(G))