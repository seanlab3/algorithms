"""
Integer base conversion algorithm
int2base(5, 2) return '101'.
base2int('F', 16) return 15.
"""

from algorithms.maths import int_to_base,base_to_int

print(int_to_base(5,2))

print(bin(5)[2:])
print(hex(15))



print(base_to_int('F',16))

print(int('0xf', 16))
