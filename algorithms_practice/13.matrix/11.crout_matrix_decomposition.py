"""
Crout matrix decomposition is used to find two matrices that, when multiplied
give our input matrix, so L * U = A.
L stands for lower and L has non-zero elements only on diagonal and below.
U stands for upper and U has non-zero elements only on diagonal and above.
This can for example be used to solve systems of linear equations.
The last if is used  if  to avoid dividing by zero.
Example:
We input the A matrix:
[[1,2,3],
[3,4,5],
[6,7,8]]
We get:
L = [1.0,  0.0, 0.0]
    [3.0, -2.0, 0.0]
    [6.0, -5.0, 0.0]
U = [1.0,  2.0, 3.0]
    [0.0,  1.0, 2.0]
    [0.0,  0.0, 1.0]
We can check that L * U = A.
I think the complexity should be O(n^3).
"""

from algorithms.matrix.crout_matrix_decomposition import crout_matrix_decomposition
A=[[1,2,3],
   [3,4,5],
   [6,7,8]]


L = [1.0,  0.0, 0.0]
[3.0, -2.0, 0.0]
[6.0, -5.0, 0.0]
U = [1.0,  2.0, 3.0]
[0.0,  1.0, 2.0]
[0.0,  0.0, 1.0]

print(crout_matrix_decomposition(A))
