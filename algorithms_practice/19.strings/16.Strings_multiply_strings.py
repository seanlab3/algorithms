"""
Given two non-negative integers num1 and num2 represented as strings,
return the product of num1 and num2.
Note:
The length of both num1 and num2 is < 110.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert
the inputs to integer directly.
"""
from algorithms.strings import multiply


print(multiply("1", "23"))
print(multiply("23", "23"))
print(multiply("100", "23"))
print(multiply("100", "10000"))