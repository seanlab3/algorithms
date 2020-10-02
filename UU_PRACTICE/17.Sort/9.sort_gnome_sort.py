from algorithms.sort import gnome_sort
import random


alist=[ random.randint(1,10) for i in range(100)]
print(alist)
sorted_list=gnome_sort(alist)
print(sorted_list)