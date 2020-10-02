"""
Insertion:
insert_one_bit(num, bit, i): insert exact one bit at specific position
For example:
Input: num = 10101 (21)
insert_one_bit(num, 1, 2): 101101 (45)
insert_one_bit(num, 0, 2): 101001 (41)
insert_one_bit(num, 1, 5): 110101 (53)
insert_one_bit(num, 1, 0): 101011 (43)
insert_mult_bits(num, bits, len, i): insert multiple bits with len at specific position
For example:
Input: num = 101 (5)
insert_mult_bits(num, 7, 3, 1): 101111 (47)
insert_mult_bits(num, 7, 3, 0): 101111 (47)
insert_mult_bits(num, 7, 3, 3): 111101 (61)
"""

"""
Insert exact one bit at specific position
Algorithm:
1. Create a mask having bit from i to the most significant bit, and append the new bit at 0 position
2. Keep the bit from 0 position to i position ( like 000...001111)
3. Merge mask and num
"""
from algorithms.bit import insert_one_bit,insert_mult_bits

num=21
print(bin(num))

b=insert_one_bit(num, 1, 2)
print(bin(b))

num=5
print(bin(num))

b=insert_mult_bits(num, 7, 3, 1)
print(bin(b))

# 박제준 5/28
