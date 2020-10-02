"""
Given a sorted array and a target value, return the index if the target is
found. If not, return the index where it would be if it were inserted in order.
For example:
[1,3,5,6], 5 -> 2
[1,3,5,6], 2 -> 1
[1,3,5,6], 7 -> 4
[1,3,5,6], 0 -> 0
"""

from algorithms.search import search_insert

a=[1,3,5,6]
k=5
print(search_insert(a,k))