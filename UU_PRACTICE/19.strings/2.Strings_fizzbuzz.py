"""
Wtite a function that returns an array containing the numbers from 1 to N,
where N is the parametered value. N will never be less than 1.
Replace certain values however if any of the following conditions are met:
If the value is a multiple of 3: use the value 'Fizz' instead
If the value is a multiple of 5: use the value 'Buzz' instead
If the value is a multiple of 3 & 5: use the value 'FizzBuzz' instead
"""

"""
There is no fancy algorithm to solve fizz buzz.
Iterate from 1 through n
Use the mod operator to determine if the current iteration is divisible by:
3 and 5 -> 'FizzBuzz'
3 -> 'Fizz'
5 -> 'Buzz'
else -> string of current iteration
return the results
Complexity:
Time: O(n)
Space: O(n)
"""

from algorithms.strings.fizzbuzz import fizzbuzz

a=[]
for i in range(2,100):
    b=fizzbuzz(i)
    a.append(b)
print(a)
