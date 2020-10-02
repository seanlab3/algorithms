from algorithms.search import linear_search
import random

alist=[random.randint(1,10) for i in range(100)]

print(alist)
print(linear_search(alist,5))