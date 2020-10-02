"""
Return list of all primes less than n,
Using sieve of Eratosthenes.
Modification:
We don't need to check all even numbers, we can make the sieve excluding even
numbers and adding 2 to the primes list by default.
We are going to make an array of: x / 2 - 1 if number is even, else x / 2
(The -1 with even number it's to exclude the number itself)
Because we just need numbers [from 3..x if x is odd]
# We can get value represented at index i with (i*2 + 3)
For example, for x = 10, we start with an array of x / 2 - 1 = 4
[1, 1, 1, 1]
 3  5  7  9
For x = 11:
[1, 1, 1, 1, 1]
 3  5  7  9  11  # 11 is odd, it's included in the list
With this, we have reduced the array size to a half,
and complexity it's also a half now.
"""
from algorithms.maths import get_primes

print(get_primes(100))