"""
Given a stack, stutter takes a stack as a parameter and  replaces every value
in the stack with two occurrences of that value.
For example, suppose the stack stores these values:
bottom [3, 7, 1, 14, 9] top
Then the stack should store these values after the method terminates:
bottom [3, 3, 7, 7, 1, 1, 14, 14, 9, 9] top
Note: There are 2 solutions:
first_stutter: it uses a single stack as auxiliary storage
second_stutter: it uses a single queue as auxiliary storage
"""

from algorithms.stack import first_stutter,second_stutter
a=[3, 7, 1, 14, 9]

print(first_stutter(a))

print(second_stutter(a))


