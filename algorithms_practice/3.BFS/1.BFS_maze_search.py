from algorithms.bfs import maze_search
"""
BFS time complexity : O(|E|)
BFS space complexity : O(|V|)
do BFS from (0,0) of the grid and get the minimum number of steps needed to get to the lower right column
only step on the columns whose value is 1
if there is no path, it returns -1


"""
a=[[1,0,1,1,1,1],
   [1,0,1,0,1,0],
   [1,0,1,0,1,1],
   [1,1,1,0,1,1]]
b=[[1,0,0],
   [0,1,1],
   [0,1,1]]

print(maze_search(a))

print(maze_search(b))