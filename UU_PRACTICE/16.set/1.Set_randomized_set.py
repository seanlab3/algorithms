"""
Design a data structure that supports all following operations
in average O(1) time.
insert(val): Inserts an item val to the set if not already present.
remove(val): Removes an item val from the set if present.
random_element: Returns a random element from current set of elements.
           Each element must have the same probability of being returned.
"""

from algorithms.set.randomized_set import RandomizedSet
import random

rset = RandomizedSet()
ground_truth = set()
n = 64

for i in range(n):
    rset.insert(i)
    ground_truth.add(i)

# Remove a half
for i in random.sample(range(n), n // 2):
    rset.remove(i)
    ground_truth.remove(i)

print(len(ground_truth), len(rset.elements), len(rset.index_map))
for i in ground_truth:
    assert(i == rset.elements[rset.index_map[i]])

for i in range(n):
    print(rset.random_element(), end=' ')
print()