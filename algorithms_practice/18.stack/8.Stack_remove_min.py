"""
Given a stack, a function remove_min accepts a stack as a parameter
and removes the smallest value from the stack.
For example:
bottom [2, 8, 3, -6, 7, 3] top
After remove_min(stack):
bottom [2, 8, 3, 7, 3] top
"""
from algorithms.stack import remove_min
a=[2, 8, 3, -6, 7, 3]

b=[2, 8, 3, 7, 3]

print(remove_min(a))


print(remove_min(b))

