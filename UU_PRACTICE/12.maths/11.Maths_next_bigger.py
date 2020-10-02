"""
I just bombed an interview and made pretty much zero
progress on my interview question.
Given a number, find the next higher number which has the
exact same set of digits as the original number.
For example: given 38276 return 38627.
             given 99999 return -1. (no such number exists)
Condensed mathematical description:
Find largest index i such that array[i − 1] < array[i].
(If no such i exists, then this is already the last permutation.)
Find largest index j such that j ≥ i and array[j] > array[i − 1].
Swap array[j] and array[i − 1].
Reverse the suffix starting at array[i].
"""
from algorithms.maths.next_bigger import next_bigger

print(next_bigger(38276))

print(next_bigger(99999))