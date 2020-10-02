from algorithms.sort import bogo_sort
import random


alist=[ random.randint(1,10) for i in range(100)]
print(alist)
sorted_list=bogo_sort(alist,simulation=False)
print(sorted_list)
