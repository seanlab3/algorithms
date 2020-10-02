"""
Given a string, find the length of the longest substring
without repeating characters.
Examples:
Given "abcabcbb", the answer is "abc", which the length is 3.
Given "bbbbb", the answer is "b", with the length of 1.
Given "pwwkew", the answer is "wke", with the length of 3.
Note that the answer must be a substring,
"pwke" is a subsequence and not a substring.
"""
from algorithms.arrays import longest_non_repeat_v1,longest_non_repeat_v2

a="abcabcbb"
b="bbbbb"
c="pwwkew"

print(longest_non_repeat_v1(a))
print(longest_non_repeat_v1(b))
print(longest_non_repeat_v1(c))

print(longest_non_repeat_v2(a))
print(longest_non_repeat_v2(b))
print(longest_non_repeat_v2(c))

### 박제준 3/11