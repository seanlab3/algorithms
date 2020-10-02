"""
Remove_bit(num, i): remove a bit at specific position.
For example:
Input: num = 10101 (21)
remove_bit(num, 2): output = 1001 (9)
remove_bit(num, 4): output = 101 (5)
remove_bit(num, 0): output = 1010 (10)
"""
from algorithms.bit import remove_bit
num=21
print(bin(num))
b=remove_bit(num, 2)
print(b)
print(bin(b))