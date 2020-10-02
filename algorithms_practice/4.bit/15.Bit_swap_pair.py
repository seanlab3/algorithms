"""
Swap_pair: A function swap odd and even bits in an integer with as few instructions
as possible (Ex bit and bit 1 are swapped, bit 2 and bit 3 are swapped)
For example:
22: 010110  --> 41: 101001
10: 1010    --> 5 : 0101
"""

"""
22: 010110  --> 41: 101001
10: 1010    --> 5 : 0101
We can approach this as operating on the odds bit first, and then the even bits.
We can mask all odd bits with 10101010 in binary ('AA') then shift them right by 1
Similarly, we mask all even bit with 01010101 in binary ('55') then shift them left
by 1. Finally, we merge these two values by OR operation.
"""
from algorithms.bit import swap_pair
n=22
print(bin(n))
print(bin(n)[2:])
b=swap_pair(n)
print(b)
print(bin(b)[2:])

## 박제준 5/25
