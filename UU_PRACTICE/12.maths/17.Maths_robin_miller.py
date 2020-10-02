"""
Rabin-Miller primality test
returning False implies that n is guaranteed composite
returning True means that n is probably prime
with a 4 ** -k chance of being wrong
"""

from algorithms.maths import is_prime

print(is_prime(12,5))