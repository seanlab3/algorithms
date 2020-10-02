"""
Suppose an array sorted in ascending order is rotated at some pivot unknown
to you beforehand. (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
Find the minimum element. The complexity must be O(logN)
You may assume no duplicate exists in the array.
"""

from algorithms.search import find_min_rotate,find_min_rotate_recur

alist=[0,1,2,3,4,5,6,7]

print(find_min_rotate(alist))


print(find_min_rotate_recur(alist,0,7))