from algorithms.dp import max_profit_naive,max_profit_optimized


a=[7, 1, 5, 3, 6, 4]
b=[7, 6, 4, 3, 1]
c = [100, 180, 260, 310, 40, 535, 695]

print(max_profit_naive(a))
print(max_profit_naive(b))
print(max_profit_naive(c))
####
print(max_profit_optimized(a))
print(max_profit_optimized(b))
print(max_profit_optimized(c))


