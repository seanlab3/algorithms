'''
Dynamic Programming
Implementation of matrix Chain Multiplication
Time Complexity: O(n^3)
Space Complexity: O(n^2)
'''

from algorithms.dp import matrix_chain_order,print_optimal_solution

array=[30,35,15,5,10,20,25]
n=len(array)
matrix , optimal_solution = matrix_chain_order(array)
print(matrix,optimal_solution)
print("No. of Operation required: "+str((matrix[1][n-1])))
print_optimal_solution(optimal_solution,1,n-1)