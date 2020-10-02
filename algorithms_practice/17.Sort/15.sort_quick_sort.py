from algorithms.sort import quick_sort
import random

alist=[random.randint(1,100) for i in range(100)]
print(alist)
sorted_list=quick_sort(alist,simulation=False)

print(sorted_list)