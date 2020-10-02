"""
Given a List of words, return the words that can be typed using letters of
alphabet on only one row's of American keyboard.
For example:
Input: ["Hello", "Alaska", "Dad", "Peace"]
Output: ["Alaska", "Dad"]
Reference: https://leetcode.com/problems/keyboard-row/description/
"""
from algorithms.set import find_keyboard_row

a=["Hello", "Alaska", "Dad", "Peace"]

print(find_keyboard_row(a))