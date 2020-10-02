"""
Given a list lst and a number N, create a new list
that contains each number of the list at most N times without reordering.
For example if N = 2, and the input is [1,2,3,1,2,1,2,3], you take [1,2,3,1,2],
drop the next [1,2] since this would lead to 1 and 2 being in the result 3 times, and then take 3,
which leads to [1,2,3,1,2,3]

[1,2,3,1,2,1,2,3]
n=2


"""

from algorithms.arrays import delete_nth_naive,delete_nth

a=[1,2,3,1,2,1,2,3]
N=2
## Time complexity O(n^2)

print(delete_nth_naive(a,N))
#Time Complexity O(n), using hash tables.

print(delete_nth(a,N))