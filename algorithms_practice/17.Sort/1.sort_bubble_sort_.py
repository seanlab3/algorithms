from algorithms.sort import bubble_sort
import random

alist=[ random.randint(1,10) for i in range(100)]
print(alist)
sorted_list=bubble_sort(alist)
print(sorted_list)
