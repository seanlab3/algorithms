"""
Given two strings s and t which consist of only lowercase letters.
String t is generated by random shuffling string s and then add one more letter
at a random position. Find the letter that was added in t.
For example:
Input:
s = "abcd"
t = "abecd"
Output: 'e'
Explanation:
'e' is the letter that was added.
"""

"""
We use the characteristic equation of XOR.
A xor B xor C = A xor C xor B
If A == C, then A xor C = 0
and then, B xor 0 =  B
"""
from algorithms.bit import find_difference

s = "abcd"
t = "abecd"

print(find_difference(s,t))
