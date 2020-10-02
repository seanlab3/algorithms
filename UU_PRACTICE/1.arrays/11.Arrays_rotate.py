"""
Rotate an array of n elements to the right by k steps.
For example, with n = 7 and k = 3,
the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].
Note:
Try to come up as many solutions as you can,
there are at least 3 different ways to solve this problem.
"""
from algorithms.arrays import rotate_v1,rotate_v2
a=[1,2,3,4,5,6,7]
k=3

print("v1==============")
print(rotate_v1(a,k))

print("v2==============")
print(rotate_v2(a,k))


from collections import deque
d=deque()
for i in range(10):
    d.append(i)

d.rotate(4)
print(d)