"""
Reverse bits of a given 32 bits unsigned integer.
For example, given input 43261596
(represented in binary as 00000010100101000001111010011100),
return 964176192
(represented in binary as 00111001011110000010100101000000).
"""
from algorithms.bit import reverse_bits
n=43261596
print(bin(n))

b=reverse_bits(n)
print(b)
print(bin(b))
