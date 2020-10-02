from algorithms.backtrack import permute,permute_iter,permute_recursive

a=[1,2,3]
b="123"
blist=[]
aperm=permute(b)
print(aperm)

bperm=permute_iter(a)
for i in bperm:
    blist.append(i)
print(blist)

print(permute_recursive(a))

#박제준 4/27
