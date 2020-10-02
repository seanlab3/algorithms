from algorithms.sort import bitonic_sort
import random
# it can only 2**n cases

alist=[ random.randint(1,10) for i in range(1024)]
print(alist)
sorted_list=bitonic_sort(alist,reverse=False)
print(sorted_list)

