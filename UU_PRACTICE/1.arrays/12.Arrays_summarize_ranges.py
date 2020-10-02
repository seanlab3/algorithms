"""
Given a sorted integer array without duplicates,
return the summary of its ranges.
For example, given [0, 1, 2, 4, 5, 7], return [(0, 2), (4, 5), (7, 7)].
"""
#https://leetcode.com/problems/summary-ranges/
"""
Example 1:

Input:  [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: 0,1,2 form a continuous range; 4,5 form a continuous range.
Example 2:

Input:  [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]
Explanation: 2,3,4 form a continuous range; 8,9 form a continuous range.

"""

from algorithms.arrays import summarize_ranges
a=[0, 1, 2, 4, 5, 7]
b=[0,2,3,4,6,8,9]


print(summarize_ranges(a))

print(summarize_ranges(b))

### 박제준 3/23