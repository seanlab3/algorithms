"""
Find missing ranges between low and high in the given array.
Ex) [3, 5] lo=1 hi=10 => answer: [(1, 2), (4, 4), (6, 10)]
"""
from algorithms.arrays import missing_ranges

a=[3,5]
lo=1
hi=10
print(missing_ranges(a,lo,hi))