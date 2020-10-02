from algorithms.sort import cocktail_shaker_sort
import random


alist=[ random.randint(1,10) for i in range(100)]
print(alist)
sorted_list=cocktail_shaker_sort(alist)
print(sorted_list)