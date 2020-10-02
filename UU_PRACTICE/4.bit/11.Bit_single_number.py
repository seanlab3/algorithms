"""
Given an array of integers, every element appears
twice except for one. Find that single one.
NOTE: This also works for finding a number occurring odd
      number of times, where all the other numbers appear
      even number of times.
Note:
Your algorithm should have a linear runtime complexity.
Could you implement it without using extra memory?
"""
## one once


from algorithms.bit import single_number
a=[4,1,2,1,2]
b=[2,2,1]

print(single_number(a))

print(single_number(b))

