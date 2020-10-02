"""
Given an array of integers nums sorted in ascending order, find the starting
and ending position of a given target value. If the target is not found in the
array, return [-1, -1].
For example:
Input: nums = [5,7,7,8,8,8,10], target = 8
Output: [3,5]
Input: nums = [5,7,7,8,8,8,10], target = 11
Output: [-1,-1]
"""

from algorithms.search import search_range
nums = [5,7,7,8,8,8,10]
target = 8

print(search_range(nums,target))