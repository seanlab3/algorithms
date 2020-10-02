"""
It's similar to how human solve Sudoku.
create a hash table (dictionary) val to store possible values in every location.
Each time, start from the location with fewest possible values, choose one value
from it and then update the board and possible values at other locations.
If this update is valid, keep solving (DFS). If this update is invalid (leaving
zero possible values at some locations) or this value doesn't lead to the
solution, undo the updates and then choose the next value.
Since we calculated val at the beginning and start filling the board from the
location with fewest possible values, the amount of calculation and thus the
runtime can be significantly reduced:
The run time is 48-68 ms on LeetCode OJ, which seems to be among the fastest
python solutions here.
The PossibleVals function may be further simplified/optimized, but it works just
fine for now. (it would look less lengthy if we are allowed to use numpy array
for the board lol).
"""
## XXXXX
from algorithms.dfs import sudoku_solver
