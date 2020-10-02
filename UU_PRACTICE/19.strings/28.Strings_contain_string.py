"""
Implement strStr().
Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
Example 1:
Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:
Input: haystack = "aaaaa", needle = "bba"
Output: -1
Reference: https://leetcode.com/problems/implement-strstr/description/
"""
from algorithms.strings import contain_string

haystack = "hello"
needle = "ll"
print(contain_string(haystack,needle))

haystack = "aaaaa"
needle = "bba"
print(contain_string(haystack,needle))



