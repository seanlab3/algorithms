"""
given input word, return the list of abbreviations.
ex)
word => [1ord, w1rd, wo1d, w2d, 3d, w3 ... etc]
"""
from algorithms.backtrack import generate_abbreviations

word=['word', 'wor1', 'wo1d', 'wo2', 'w1rd', 'w1r1', 'w2d', 'w3', '1ord', '1or1', '1o1d', '1o2', '2rd', '2r1', '3d', '4']
word2=['word', 'wor1', 'wo1d' ]
print(generate_abbreviations(word))

print(generate_abbreviations(word2))