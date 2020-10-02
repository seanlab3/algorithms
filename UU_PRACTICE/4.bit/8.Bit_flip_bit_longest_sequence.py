"""
You have an integer and you can flip exactly one bit from a 0 to 1.
Write code to find the length of the longest sequence of 1s you could create.
For example:
Input: 1775 ( or: 11011101111)
Output: 8
"""
from algorithms.bit import flip_bit_longest_seq

n=1775
print(bin(n))

print(flip_bit_longest_seq(n))
