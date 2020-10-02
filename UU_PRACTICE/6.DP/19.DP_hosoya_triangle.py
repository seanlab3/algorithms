"""
Hosoya triangle (originally Fibonacci triangle) is a triangular arrangement
of numbers, where if you take any number it is the sum of 2 numbers above.
First line is always 1, and second line is always {1     1}.
This printHosoya function takes argument n which is the height of the triangle
(number of lines).
For example:
printHosoya( 6 ) would return:
1
1 1
2 1 2
3 2 2 3
5 3 4 3 5
8 5 6 6 5 8
The complexity is O(n^3).
"""
from algorithms.dp import print_hosoya

print_hosoya(10)