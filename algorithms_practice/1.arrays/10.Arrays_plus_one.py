"""
Given a non-negative number represented as an array of digits,
adding one to each numeral.
The digits are stored big-endian, such that the most significant
digit is at the head of the list.

a=[1,2,3]
b=[9,9,9,9]


[1, 2, 4]
[1, 0, 0, 0, 0]
"""
#https://leetcode.com/problems/plus-one/
from algorithms.arrays import plus_one_v1,plus_one_v2

a=[1,2,3]
b=[9,9,9,9]
print("v1=============")
print(plus_one_v1(a))
print(plus_one_v1(b))
print("v2=============")
print(plus_one_v2(a))
print(plus_one_v2(b))



## 박제준 3/18

## 김 서현 5/24



