from algorithms.sort import bucket_sort
import random


alist=[ random.randint(1,10) for i in range(100)]
print(alist)
sorted_list=bucket_sort(alist)
print(sorted_list)
