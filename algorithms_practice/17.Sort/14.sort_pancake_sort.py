from algorithms.sort import pancake_sort
import random

alist=[random.randint(1,100) for i in range(100)]
print(alist)
sorted_list=pancake_sort(alist)
print(sorted_list)