#
# Search a key in a row wise and column wise sorted (non-decreasing) matrix.
# m- Number of rows in the matrix
# n- Number of columns in the matrix
# T(n)- O(m+n)
#

from algorithms.matrix.search_in_sorted_matrix import search_in_a_sorted_matrix

mat = [
    [2, 5, 7],
    [4, 8, 13],
    [9, 11, 15],
    [12, 17, 20]
]
key = 13
print (mat)
search_in_a_sorted_matrix(mat, len(mat), len(mat[0]), key)