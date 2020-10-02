"""
Given a positive integer N and a precision factor P,
it produces an output
with a maximum error P from the actual square root of N.
Example:
Given N = 5 and P = 0.001, can produce output x such that
2.235 < x < 2.237. Actual square root of 5 being 2.236.
"""

from algorithms.maths.sqrt_precision_factor import square_root


print(square_root(5))