"""
Sometimes you need to limit array result to use. Such as you only need the
 value over 10 or, you need value under than 100. By use this algorithms, you
 can limit your array to specific value
If array, Min, Max value was given, it returns array that contains values of
 given array which was larger than Min, and lower than Max. You need to give
 'unlimit' to use only Min or Max.
ex) limit([1,2,3,4,5], None, 3) = [1,2,3]
Complexity = O(n)
"""
from algorithms.arrays import limit
import random

alist=[random.randint(1,10) for i in range(100)]

print(limit(alist))

print(limit(alist,5,7))


print(limit(alist,1,7))