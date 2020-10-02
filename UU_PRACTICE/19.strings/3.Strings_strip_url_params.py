"""
Write a function that does the following:
Removes any duplicate query string parameters from the url
Removes any query string parameters specified within the 2nd argument (optional array)
An example:
www.saadbenn.com?a=1&b=2&a=2') // returns 'www.saadbenn.com?a=1&b=2'
"""
from algorithms.strings import strip_url_params1,strip_url_params2,strip_url_params3

a="www.saadbenn.com?a=1&b=2&a=2')"

print(strip_url_params1(a))

print(strip_url_params2(a))


print(strip_url_params3(a))