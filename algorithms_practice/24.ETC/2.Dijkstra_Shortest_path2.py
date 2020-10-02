import sys
INT_MAX = sys.maxsize
INT_MIN = -sys.maxsize-1

class Graph():

    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]

    # A utility function to find the vertex with
    # minimum distance value, from the set of vertices
    # not yet included in shortest path tree
    def minDistance(self, dist, sptSet):

        # Initilaize minimum distance for next node
        #min = sys.maxint
        min = INT_MAX

        # Search not nearest vertex not in the
        # shortest path tree
        for v in range(self.V):
            if dist[v] < min and sptSet[v] == False:
                min = dist[v]
                min_index = v

        return min_index


    def dijkstra(self, src):

        #dist = [sys.maxint] * self.V
        dist = [INT_MAX] * self.V
        dist[src] = 0
        sptSet = [False] * self.V

        for cout in range(self.V):

            # Pick the minimum distance vertex from
            # the set of vertices not yet processed.
            # u is always equal to src in first iteration
            u = self.minDistance(dist, sptSet)

            # Put the minimum distance vertex in the
            # shotest path tree
            sptSet[u] = True

            # Update dist value of the adjacent vertices
            # of the picked vertex only if the current
            # distance is greater than new distance and
            # the vertex in not in the shotest path tree
            for v in range(self.V):
                if self.graph[u][v] > 0 and sptSet[v] == False and \
                        dist[v] > dist[u] + self.graph[u][v]:
                    dist[v] = dist[u] + self.graph[u][v]

        #self.printSolution(dist)

        return dist


n,m=map(int,input().split())
g = Graph(n)
# 0 47 69 0 0 0 0
# 0 0 0 57 124 0 0
# 0 0 0 37 59 86 0
# 0 0 0 0 0 27 94
# 0 0 0 0 0 0 21
# 0 0 0 0 0 0 40
# 0 0 0 0 0 0 0
#g.graph=[ [0 for i in range(n)] for j in range(n)]
# for i in g.graph:
#     for j in i:
#         print(j,end=" ")
#     print()
for i in range(m):
    a,b,c=map(int,input().split())
    g.graph[a-1][b-1]=c

# for i in g.graph:
#     for j in i:
#         print(j,end=" ")
#     print()

a=g.dijkstra(0)
if len(a)==0:
    print(-1)
else:
    print(a[-1])

"""
7 11
1 2 47
1 3 69
2 4 57
2 5 124
3 4 37
3 5 59
3 6 86
4 6 27
4 7 94
5 7 21
6 7 40

149


7 11
1 2 3
1 3 12
2 4 58
2 5 136
3 4 32
3 5 54
3 6 88
4 6 23
4 7 91
5 7 17
6 7 5

72


"""
