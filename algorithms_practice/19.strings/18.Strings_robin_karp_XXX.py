
###  XXXX
from algorithms.strings import rabin_karp
###
txt = "GEEKS FOR GEEKS"
pat = "GEEK"

a="ABAAABCDBBABCDDEBCABC"
b="ABC"

print(rabin_karp(txt,pat))

print(rabin_karp(a,b))