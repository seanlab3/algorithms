"""
Find missing ranges between low and high in the given array.
Ex) [3, 5] lo=1 hi=10 => answer: [(1, 2), (4, 4), (6, 10)]
"""
def missing_ranges(arr, lo, hi):

    res = []
    start = lo

    for n in arr:

        if n == start:
            start += 1
        elif n > start:
            res.append((start, n-1))
            start = n + 1

    if start <= hi:
        res.append((start, hi))

    return res
a=[3,5]
lo=1
hi=10
print(missing_ranges(a,lo,hi))
from algorithms.arrays import missing_ranges

a=[3,5]
lo=1
hi=10
print(missing_ranges(a,lo,hi))