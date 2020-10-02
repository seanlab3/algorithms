"""
do BFS from each building, and decrement all empty place for every building visit
when grid[i][j] == -b_nums, it means that grid[i][j] are already visited from all b_nums
and use dist to record distances from b_nums
"""
from algorithms.bfs import shortest_distance_from_all_building
## if  1 <==> 1
grid = [[1, 0, 2, 0, 1],
        [0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0]]

print(shortest_distance_from_all_building(grid))