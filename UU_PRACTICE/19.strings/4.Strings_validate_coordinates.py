""""
Create a function that will validate if given parameters are valid geographical coordinates.
Valid coordinates look like the following: "23.32353342, -32.543534534". The return value should be either true or false.
Latitude (which is first float) can be between 0 and 90, positive or negative. Longitude (which is second float) can be between 0 and 180, positive or negative.
Coordinates can only contain digits, or one of the following symbols (including space after comma) -, .
There should be no space between the minus "-" sign and the digit after it.
Here are some valid coordinates:
-23, 25
43.91343345, 143
4, -3
And some invalid ones:
23.234, - 23.4234
N23.43345, E32.6457
6.325624, 43.34345.345
0, 1,2
"""
from algorithms.strings import is_valid_coordinates_0,is_valid_coordinates_1,is_valid_coordinates_regular_expression
coordinates1="-23, 25"

coordinates2="43.91343345, 143"


coordinates3="4, -3"

coordinates4="23.234, - 23.4234"

print(is_valid_coordinates_0(coordinates1))
print(is_valid_coordinates_1(coordinates1))
print(is_valid_coordinates_regular_expression(coordinates1))

print(is_valid_coordinates_0(coordinates2))
print(is_valid_coordinates_1(coordinates2))
print(is_valid_coordinates_regular_expression(coordinates2))


print(is_valid_coordinates_0(coordinates3))
print(is_valid_coordinates_1(coordinates3))
print(is_valid_coordinates_regular_expression(coordinates3))



print(is_valid_coordinates_0(coordinates4))
print(is_valid_coordinates_1(coordinates4))
print(is_valid_coordinates_regular_expression(coordinates4))
