from algorithms.sort import max_heap_sort
import random
#ascending order

alist=[ random.randint(1,10) for i in range(100)]
print(alist)
sorted_list=max_heap_sort(alist)
print(sorted_list)