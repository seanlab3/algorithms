"""
Given a positive integer, check whether it has alternating bits: namely,
if two adjacent bits will always have different values.
For example:
Input: 5
Output: True because the binary representation of 5 is: 101.
Input: 7
Output: False because the binary representation of 7 is: 111.
Input: 11
Output: False because the binary representation of 11 is: 1011.
Input: 10
Output: True because The binary representation of 10 is: 1010.
"""
from algorithms.bit import has_alternative_bit,has_alternative_bit_fast

n=5
print(has_alternative_bit(n))

print(has_alternative_bit_fast(n))
n=7

print(has_alternative_bit(n))

print(has_alternative_bit_fast(n))
