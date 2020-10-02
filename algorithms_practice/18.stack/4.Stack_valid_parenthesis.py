"""
Given a string containing just the characters
'(', ')', '{', '}', '[' and ']',
determine if the input string is valid.
The brackets must close in the correct order,
"()" and "()[]{}" are all valid but "(]" and "([)]" are not.
"""

from algorithms.stack.valid_parenthesis import is_valid

a="{{}()[)]}"

b="{[]([]())}"

print(is_valid(a))

print(is_valid(b))