"""
    Returns the missing number from a sequence of unique integers
    in range [0..n] in O(n) time and space. The difference between
    consecutive integers cannot be more than 1. If the sequence is
    already complete, the next integer in the sequence will be returned.
    For example:
    Input: nums = [4, 1, 3, 0, 6, 5, 2]
    Output: 7
"""
from algorithms.bit import find_missing_number,find_missing_number2

nums = [4, 1, 3, 0, 6, 5, 2]

print(find_missing_number(nums))

print(find_missing_number2(nums))

#박제준 5/14
