"""
This algorithm takes two compatible two dimensional matrix
and return their product
Space complexity: O(n^2)
Possible edge case: the number of columns of multiplicand not consistent with
the number of rows of multiplier, will raise exception
"""

###two compatible two dimensional matrix


from algorithms.matrix.multiply import multiply

alist=[[3,4],[3,4]]
blist=[[1,2],[3,4]]

print(multiply(alist,blist))