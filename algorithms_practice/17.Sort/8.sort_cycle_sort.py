from algorithms.sort import cycle_sort
import random


alist=[ random.randint(1,10) for i in range(100)]
print(alist)
sorted_list=cycle_sort(alist)
print(sorted_list)