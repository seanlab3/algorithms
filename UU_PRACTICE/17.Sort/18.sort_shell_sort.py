from algorithms.sort import shell_sort
import random
alist=[random.randint(1,100) for i in range(100)]
print(alist)
sorted_list=shell_sort(alist)
print(sorted_list)