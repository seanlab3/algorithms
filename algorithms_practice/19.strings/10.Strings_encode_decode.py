""" Design an algorithm to encode a list of strings to a string.
 The encoded mystring is then sent over the network and is decoded
 back to the original list of strings.
"""
from algorithms.strings import encode,decode

alist="ab bc cd ef"

b=encode(alist)
print(b)

c=decode(b)
print(c)