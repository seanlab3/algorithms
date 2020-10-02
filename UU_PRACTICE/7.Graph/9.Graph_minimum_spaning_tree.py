from algorithms.graph.minimum_spanning_tree import Edge,DisjointSet,kruskal
"""
5 6
1 2 3
1 3 8
2 4 5
3 4 2
3 5 4
4 5 6

"""
# 5 6
# 1 2 3
# 1 3 8
# 2 4 5
# 3 4 2
# 3 5 4
# 4 5 6
from algorithms.graph.minimum_spanning_tree import Edge,DisjointSet,kruskal
import sys
for n_m in sys.stdin:
    n, m = map(int, n_m.split())
    ds = DisjointSet(m)
    edges = [None] * m # Create list of size <m>

    # Read <m> edges from input
    for i in range(m):
        u, v, weight = map(int, input().split())
        u -= 1 # Convert from 1-indexed to 0-indexed
        v -= 1 # Convert from 1-indexed to 0-indexed
        edges[i] = Edge(u, v, weight)

    # After finish input and graph creation, use Kruskal algorithm for MST:
    print("MST weights sum:", kruskal(n, edges, ds))
