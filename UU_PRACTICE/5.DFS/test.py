n=int(input())
alist=[]
while n>2:
    for i in range(2,n):
        if n%i==0:
            alist.append([i,n//i])
            n=n//i
            print(n)
            break
print(alist)
