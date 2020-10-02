"""
Given a non-empty string check if it can be constructed by taking
a substring of it and appending multiple copies of the substring together.
For example:
Input: "abab"
Output: True
Explanation: It's the substring "ab" twice.
Input: "aba"
Output: False
Input: "abcabcabcabc"
Output: True
Explanation: It's the substring "abc" four times.
Reference: https://leetcode.com/problems/repeated-substring-pattern/description/
"""
from algorithms.strings import repeat_substring

a="abab"

b="aba"

c="abcabcabcabc"

print(repeat_substring(a))

print(repeat_substring(b))

print(repeat_substring(c))


