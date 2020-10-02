"""
You are given two non-empty linked lists representing
two non-negative integers. The digits are stored in reverse order
and each of their nodes contain a single digit.
Add the two numbers and return it as a linked list.
You may assume the two numbers do not contain any leading zero,
except the number 0 itself.
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
"""

from algorithms.linkedlist.add_two_numbers import Node,TestSuite,add_two_numbers,convert_to_str

# 1. test case
number1 = Node(2)
number1.next = Node(4)
number1.next.next = Node(3)

number2 = Node(5)
number2.next = Node(6)
number2.next.next = Node(4)
result = convert_to_str(add_two_numbers(number1, number2))
print(result)