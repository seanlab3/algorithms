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
def plus_one_v1(digits):
    """
    :type digits: List[int]
    :rtype: List[int]
    """
    digits[-1] = digits[-1] + 1
    res = []
    ten = 0
    i = len(digits)-1
    while i >= 0 or ten == 1:
        summ = 0
        if i >= 0:
            summ += digits[i]
        if ten:
            summ += 1
        res.append(summ % 10)
        ten = summ // 10
        i -= 1
    return res[::-1]


def plus_one_v2(digits):
    n = len(digits)
    for i in range(n-1, -1, -1):
        if digits[i] < 9:
            digits[i] += 1
            return digits
        digits[i] = 0
    digits.insert(0, 1)
    return digits


def plus_one_v3(num_arr):

    for idx, digit in reversed(list(enumerate(num_arr))):
        num_arr[idx] = (num_arr[idx] + 1) % 10
        if num_arr[idx]:
            return num_arr
    return [1] + num_arr

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



