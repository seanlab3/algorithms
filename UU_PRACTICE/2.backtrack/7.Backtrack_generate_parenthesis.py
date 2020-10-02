"""

Given n pairs of parentheses, write a function to generate
all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
    "((()))",
    "(()())",
    "(())()",
    "()(())",
    "()()()"
]

"""

from algorithms.backtrack import generate_parenthesis

n=3
n2=5
print(generate_parenthesis(n))

print(generate_parenthesis(n2))