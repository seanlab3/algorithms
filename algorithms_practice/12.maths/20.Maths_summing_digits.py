"""
Recently, I encountered an interview question whose description was as below:
The number 89 is the first integer with more than one digit whose digits when raised up to consecutive powers give the same
number. For example, 89 = 8**1 + 9**2 gives the number 89.
The next number after 89 with this property is 135 = 1**1 + 3**2 + 5**3 = 135.
Write a function that returns a list of numbers with the above property. The function will receive range as parameter.
"""

from algorithms.maths.summing_digits import sum_dig_pow


print(sum_dig_pow(1, 10))

print(sum_dig_pow(1, 100))
