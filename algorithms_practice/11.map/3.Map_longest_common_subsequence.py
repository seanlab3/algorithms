"""
Given string a and b, with b containing all distinct characters,
find the longest common sub sequence's length.
Expected complexity O(n logn).
"""
from algorithms.map.longest_common_subsequence import max_common_sub_string

a="AGGTAB"
b="GXTAYB"
print(max_common_sub_string(a,b))