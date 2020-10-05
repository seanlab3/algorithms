"""
Implement Flatten Arrays.
Given an array that may contain nested arrays,
produce a single resultant array.
"""
from collections import Iterable


# return list
def flatten(input_arr, output_arr=None):
    if output_arr is None:
        output_arr = []
    for ele in input_arr:
        if isinstance(ele, Iterable):
            flatten(ele, output_arr)
        else:
            output_arr.append(ele)
    return output_arr


# returns iterator
def flatten_iter(iterable):
    """
    Takes as input multi dimensional iterable and
    returns generator which produces one dimensional output.
    """
    for element in iterable:
        if isinstance(element, Iterable):
            yield from flatten_iter(element)
        else:
            yield element

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