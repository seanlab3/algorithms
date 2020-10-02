"""
Given an unsorted array of integers, find the length of longest increasing subsequence.
Example:
Input: [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
The time complexity is O(n^2).
"""

from algorithms.dp import longest_increasing_subsequence

a=[10,9,2,5,3,7,101,18]

print(longest_increasing_subsequence(a))
