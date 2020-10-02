"""
Find the index of 0 to be replaced with 1 to get
longest continuous sequence
of 1s in a binary array.
Returns index of 0 to be
replaced with 1 to get longest
continuous sequence of 1s.
If there is no 0 in array, then
it returns -1.
e.g.
let input array = [1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1]
If we replace 0 at index 3 with 1, we get the longest continuous
sequence of 1s in the array.
So the function return => 3
"""
from algorithms.arrays import max_ones_index
import random
#1110, 1, 1, 1, 1, 1, 0, 1, 1, 1
array = [1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1]
blist=[1,1,1,1,1,1,0]
print(max_ones_index(array))
alist=[ random.choice(blist) for i in range(100) ]
print(alist)

print(max_ones_index(array))

def max_ones_index2(array2):
    count=0
    for i in range(len(array2)):
        if array2[i]==1:
            count+=1
        elif array2[i]==0:
            alist.append([count,i])
            count=0
    maxa=0
    maxindex=0
    for i in range(len(alist)-1):
        if alist[i][0]+alist[i+1][0]>maxa:
            maxa=alist[i][0]+alist[i+1][0]
            maxindex=alist[i][1]
    print(maxindex)


array = [1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1]
alist=[]
#
import random
blist=[1,1,1,1,1,1,0,0,0]
clist=[ random.choice(blist) for i in range(100) ]
print(clist)
array=array+[0]

array2=clist+[0]
print(max_ones_index(array2))


print(max_ones_index2(array2))