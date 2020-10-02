from algorithms.maths import combination,combination_memo

print(combination(5,3))

print(combination_memo(5,3))

from itertools import combinations

alist=[i for i in range(5)]
comb=combinations(alist,3)
count=0
for i in comb:
    print(i)
    count+=1
print(count)