"""
Given two strings s and t , write a function to determine if t is an anagram of s.
Example 1:
Input: s = "anagram", t = "nagaram"
Output: true
Example 2:
Input: s = "rat", t = "car"
Output: false
Note:
You may assume the string contains only lowercase alphabets.
Reference: https://leetcode.com/problems/valid-anagram/description/
"""
from algorithms.map import is_anagram

s = "anagram"
t = "nagaram"
print(is_anagram(s,t))


