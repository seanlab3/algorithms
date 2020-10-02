"""
Write an algorithm that takes an array and moves all of the zeros to the end,
preserving the order of the other elements.
    move_zeros([false, 1, 0, 1, 2, 0, 1, 3, "a"])
    returns => [false, 1, 1, 2, 1, 3, "a", 0, 0]
The time complexity of the below algorithm is O(n).
"""
from algorithms.arrays import move_zeros

a=[False, 1, 0, 1, 2, 0, 1, 3, "a"]

print(move_zeros(a))
