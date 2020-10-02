"""
Given a strings s and int k, return a string that rotates k times
For example,
rotate("hello", 2) return "llohe"
rotate("hello", 5) return "hello"
rotate("hello", 6) return "elloh"
rotate("hello", 7) return "llohe"
accepts two strings
returns bool
"""

from algorithms.strings import rotate

print(rotate("hello", 2)) #return "llohe"
print(rotate("hello", 5)) #return "hello"
print(rotate("hello", 6)) #return "elloh"
print(rotate("hello", 7)) #return "llohe"