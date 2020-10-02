"""
Given a stack, a function is_consecutive takes a stack as a parameter and that
returns whether or not the stack contains a sequence of consecutive integers
starting from the bottom of the stack (returning true if it does, returning
false if it does not).
For example:
bottom [3, 4, 5, 6, 7] top
Then the call of is_consecutive(s) should return true.
bottom [3, 4, 6, 7] top
Then the call of is_consecutive(s) should return false.
bottom [3, 2, 1] top
The function should return false due to reverse order.
Note: There are 2 solutions:
first_is_consecutive: it uses a single stack as auxiliary storage
second_is_consecutive: it uses a single queue as auxiliary storage
"""
from algorithms.stack import first_is_consecutive,second_is_consecutive
a=[3, 4, 5, 6, 7]

print(first_is_consecutive(a))

print(second_is_consecutive(a))

b=[3, 4, 6, 7]

print(first_is_consecutive(b))

print(second_is_consecutive(b))



