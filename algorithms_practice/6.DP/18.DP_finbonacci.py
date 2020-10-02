from algorithms.dp import fib_recursive,fib_list,fib_iter
from eulerlib import fibo_num_digits

def finbonacci_iter(n):
    fib1=0
    fib2=1
    sum=0
    if n<=1:
        return n
    for _ in range(n-1):
        sum=fib1+fib2
        fib1=fib2
        fib2=sum
    return sum

def fibonacci2(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


n=20
print(fib_recursive(n))

n=100
print(fib_list(n))

n=100
print(fib_iter(n))


n=1000
print(finbonacci_iter(n))

print(fibonacci2(n))

#print(fibo_num_digits(n))

