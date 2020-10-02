'''
Given a list of sorted characters letters containing only lowercase letters,
and given a target letter target, find the smallest element in the list that
is larger than the given target.
Letters also wrap around. For example, if the target is target = 'z' and
letters = ['a', 'b'], the answer is 'a'.
Input:
letters = ["c", "f", "j"]
target = "a"
Output: "c"
Input:
letters = ["c", "f", "j"]
target = "c"
Output: "f"
Input:
letters = ["c", "f", "j"]
target = "d"
Output: "f"
Reference: https://leetcode.com/problems/find-smallest-letter-greater-than-target/description/
'''
from algorithms.search import next_greatest_letter,next_greatest_letter_v1,next_greatest_letter_v2
letters = ["c", "f", "j"]
target = "a"

print(next_greatest_letter(letters,target))


print(next_greatest_letter_v1(letters,target))


print(next_greatest_letter_v2(letters,target))




