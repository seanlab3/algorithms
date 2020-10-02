"""
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".
Example 1:
Input: ["flower","flow","flight"]
Output: "fl"
Example 2:
Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Reference: https://leetcode.com/problems/longest-common-prefix/description/
"""
from algorithms.strings import longest_common_prefix_v1,longest_common_prefix_v2,longest_common_prefix_v3


a=["flower","flow","flight"]

"""
First solution: Horizontal scanning
"""
print(longest_common_prefix_v1(a))
"""
Second solution: Vertical scanning
"""
print(longest_common_prefix_v2(a))
"""
Third solution: Divide and Conquer
"""
print(longest_common_prefix_v3(a))

b=["dog","racecar","car"]

"""
First solution: Horizontal scanning
"""
print(longest_common_prefix_v1(b))
"""
Second solution: Vertical scanning
"""
print(longest_common_prefix_v2(b))
"""
Third solution: Divide and Conquer
"""
print(longest_common_prefix_v3(b))

