"""
Write a function that when given a URL as a string, parses out just the domain name and returns it as a string.
Examples:
domain_name("http://github.com/SaadBenn") == "github"
domain_name("http://www.zombie-bites.com") == "zombie-bites"
domain_name("https://www.cnet.com") == "cnet"
Note: The idea is not to use any built-in libraries such as re (regular expression) or urlparse except .split() built-in function
"""
from algorithms.strings import domain_name_1,domain_name_2

a="http://github.com/SaadBenn"

print(domain_name_1(a))

print(domain_name_2(a))