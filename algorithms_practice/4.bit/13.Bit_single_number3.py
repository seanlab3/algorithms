"""
Given an array of numbers nums,
in which exactly two elements appear only once
and all the other elements appear exactly twice.
Find the two elements that appear only once.
Limitation: Time Complexity: O(N) and Space Complexity O(1)
For example:
Given nums = [1, 2, 1, 3, 2, 5], return [3, 5].
Note:
The order of the result is not important.
So in the above example, [5, 3] is also correct.
Solution:
1. Use XOR to cancel out the pairs and isolate A^B
2. It is guaranteed that at least 1 bit exists in A^B since
   A and B are different numbers. ex) 010 ^ 111 = 101
3. Single out one bit R (right most bit in this solution) to use it as a pivot
4. Divide all numbers into two groups.
   One group with a bit in the position R
   One group without a bit in the position R
5. Use the same strategy we used in step 1 to isolate A and B from each group.
"""

# Two element once
from algorithms.bit import single_number,single_number2,single_number3

nums = [1, 2, 1, 3, 2, 5]

print(single_number(nums))  ## XXX
print(single_number2(nums))  ## XXX

print(single_number3(nums))