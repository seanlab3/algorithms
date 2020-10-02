"""
Given an api which returns an array of words and an array of symbols, display
the word with their matched symbol surrounded by square brackets.
If the word string matches more than one symbol, then choose the one with
longest length. (ex. 'Microsoft' matches 'i' and 'cro'):
Example:
Words array: ['Amazon', 'Microsoft', 'Google']
Symbols: ['i', 'Am', 'cro', 'Na', 'le', 'abc']
Output:
[Am]azon, Mi[cro]soft, Goog[le]
My solution(Wrong):
(I sorted the symbols array in descending order of length and ran loop over
words array to find a symbol match(using indexOf in javascript) which
worked. But I didn't make it through the interview, I am guessing my solution
was O(n^2) and they expected an efficient algorithm.
output:
['[Am]azon', 'Mi[cro]soft', 'Goog[le]', 'Amaz[o]n', 'Micr[o]s[o]ft', 'G[o][o]gle']
"""
from algorithms.strings import match_symbol,match_symbol_1
a=['Amazon', 'Microsoft', 'Google']
s=['i', 'Am', 'cro', 'Na', 'le', 'abc']

print(match_symbol(a,s))

print(match_symbol_1(a,s))