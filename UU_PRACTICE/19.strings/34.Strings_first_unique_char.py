"""
Given a string, find the first non-repeating character in it and return it's
index. If it doesn't exist, return -1.
For example:
s = "leetcode"
return 0.
s = "loveleetcode",
return 2.
Reference: https://leetcode.com/problems/first-unique-character-in-a-string/description/
"""
from algorithms.strings import first_unique_char


s1 = "leetcode"

s2 = "loveleetcode"

print(first_unique_char(s1))


print(first_unique_char(s2))