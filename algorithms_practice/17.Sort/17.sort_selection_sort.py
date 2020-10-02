from algorithms.sort import selection_sort
import random
alist=[random.randint(1,100) for i in range(10)]
print(alist)
sorted_list=selection_sort(alist,simulation=True)
print(sorted_list)