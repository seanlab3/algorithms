from algorithms.dfs import get_factors,get_factors_iterative1,get_factors_iterative2
"""
Numbers can be regarded as product of its factors. For example,
8 = 2 x 2 x 2;
  = 2 x 4.
Write a function that takes an integer n and return all possible combinations
of its factors.Numbers can be regarded as product of its factors. For example,
8 = 2 x 2 x 2;
  = 2 x 4.
Examples:
input: 1
output:
[]
input: 37
output:
[]
input: 32
output:
[
  [2, 16],
  [2, 2, 8],
  [2, 2, 2, 4],
  [2, 2, 2, 2, 2]
]

[[2, 16], [2, 2, 8], [2, 2, 2, 4], [2, 2, 2, 2, 2], [2, 4, 4], [4, 8]]

"""
n=37
n2=32
print(get_factors(37))

print(get_factors(32))


print(get_factors_iterative1(37))

print(get_factors_iterative2(32))

################################
"""
## 소인수분해 
n=int(input())
alist=[]
while n>=2:
    for i in range(2,n):
        if n%i==0:
            alist.append(i)
            n=n//i
            #print(n)
            break
print(alist)
"""
