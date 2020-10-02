"""
Write a function to determine the minimal number of bits you would need to
flip to convert integer A to integer B.
For example:
Input: 29 (or: 11101), 15 (or: 01111)
Output: 2
"""
from algorithms.bit import count_flips_to_convert
a=29
b=15

print(count_flips_to_convert(a,b))

##박제준 5/11
