"""
Write a function that takes an unsigned integer and
returns the number of '1' bits it has
(also known as the Hamming weight).
For example, the 32-bit integer '11' has binary
representation 00000000000000000000000000001011,
so the function should return 3.
T(n)- O(k)   : k is the number of 1s present in binary representation.
NOTE: this complexity is better than O(log n).
e.g. for n = 00010100000000000000000000000000
only 2 iterations are required.
Number of loops is
equal to the number of 1s in the binary representation.
"""
from algorithms.bit import count_ones_iter,count_ones_recur
n=11

print(count_ones_iter(n))
print(count_ones_recur(n))

