"""
Given an array of strings, group anagrams together.
For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"],
Return:
[
  ["ate", "eat","tea"],
  ["nat","tan"],
  ["bat"]
]
"""
from algorithms.strings import group_anagrams

a=["eat", "tea", "tan", "ate", "nat", "bat"]

print(group_anagrams(a))