from algorithms.search import last_occurrence
import random

alist=[random.randint(1,10) for i in range(100)]

print(alist)
print(last_occurrence(alist,5))