from algorithms.search import binary_search,binary_search_recur
import random

alist=[random.randint(1,5) for i in range(100)]
print(alist)
print(binary_search(alist,4))

blist=[random.randint(1,5) for i in range(100)]
print(binary_search_recur(blist,40,80,5))