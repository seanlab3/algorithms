"""
Given two words word1 and word2, find the minimum number of steps required to
make word1 and word2 the same, where in each step you can delete one character
in either string.
For example:
Input: "sea", "eat"
Output: 2
Explanation: You need one step to make "sea" to "ea" and another step to make "eat" to "ea".
Reference: https://leetcode.com/problems/delete-operation-for-two-strings/description/
"""

from algorithms.strings import min_distance,lcs

word1="sea"
word2="eat"

print(min_distance(word1,word2))

