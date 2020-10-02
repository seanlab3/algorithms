#
# Count the number of unique paths from a[0][0] to a[m-1][n-1]
# We are allowed to move either right or down from a cell in the matrix.
# Approaches-
# (i) Recursion- Recurse starting from a[m-1][n-1], upwards and leftwards,
#                add the path count of both recursions and return count.
# (ii) Dynamic Programming- Start from a[0][0].Store the count in a count
#                           matrix. Return count[m-1][n-1]
# T(n)- O(mn), S(n)- O(mn)
#
from algorithms.matrix.count_paths import count_paths
m, n = map(int, input('Enter two positive integers: ').split())
count_paths(m, n)