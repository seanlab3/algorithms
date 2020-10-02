"""
Atbash cipher is mapping the alphabet to it's reverse.
So if we take "a" as it is the first letter, we change it to the last - z.
Example:
Attack at dawn --> Zggzxp zg wzdm
Complexity: O(n)
"""

from algorithms.strings import atbash

a="Attack at dawn"
print(atbash(a))