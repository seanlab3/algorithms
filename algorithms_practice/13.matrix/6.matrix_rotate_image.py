"""
You are given an n x n 2D mat representing an image.
Rotate the image by 90 degrees (clockwise).
Follow up:
Could you do this in-place?
"""


# clockwise rotate
# first reverse up to down, then swap the symmetry
# 1 2 3     7 8 9     7 4 1
# 4 5 6  => 4 5 6  => 8 5 2
# 7 8 9     1 2 3     9 6 3
from algorithms.matrix.rotate_image import rotate

mat = [[1,2,3],
       [4,5,6],
       [7,8,9]]
print(mat)
rotate(mat)
print(mat)

