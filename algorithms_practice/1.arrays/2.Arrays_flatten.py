"""
Implement Flatten Arrays.
Given an array that may contain nested arrays,
produce a single resultant array.
"""

from algorithms.arrays import flatten,flatten_iter

a=[1,2,3,[2,3,5, [5,8,3]]]
#out=[1, 2, 3, 2, 3, 5, 5, 8, 3]

print(flatten(a))

c=[]
for i in flatten_iter(a):
    #print(i)
    c.append(i)
print(c)


b=str(a)
alist=[]
for i in b:
    if i.isdigit():
        alist.append(int(i))


### 김서현 5/10

## 강민서 7/30