"""
Given a string, determine if it is a palindrome,
considering only alphanumeric characters and ignoring cases.
For example,
"A man, a plan, a canal: Panama" is a palindrome.
"race a car" is not a palindrome.
Note:
Have you consider that the string might be empty?
This is a good question to ask during an interview.
For the purpose of this problem,
we define empty string as valid palindrome.
"""

from algorithms.strings import is_palindrome,remove_punctuation,is_palindrome_reverse,is_palindrome_two_pointer,is_palindrome_stack


s="abcdcba"

print(is_palindrome(s))

print(is_palindrome_reverse(s))

print(is_palindrome_two_pointer(s))

print(is_palindrome_stack(s))


