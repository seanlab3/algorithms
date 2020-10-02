"""
Given an array of integers, return indices of the two numbers
such that they add up to a specific target.
You may assume that each input would have exactly one solution,
and you may not use the same element twice.
Example:
    Given nums = [2, 7, 11, 15], target = 9,
    Because nums[0] + nums[1] = 2 + 7 = 9,
    return (0, 1)
"""
import random
alist=[random.randrange(1,10) for i in range(50)]
k=random.randint(1,10)

from algorithms.arrays import two_sum
a=[2, 7, 11, 15]
target=9

print(two_sum(a,9))
print(alist)
alist=list(set(alist))
print(alist)
print(k)
print(two_sum(alist,k))

### 박제준 4/1