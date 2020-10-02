"""
Given the capacity of the knapsack and items specified by weights and values,
return the maximum summarized value of the items that can be fit in the
knapsack.
Example:
capacity = 5, items(value, weight) = [(60, 5), (50, 3), (70, 4), (30, 2)]
result = 80 (items valued 50 and 30 can both be fit in the knapsack)
The time complexity is O(n * m) and the space complexity is O(m), where n is
the total number of items and m is the knapsack's capacity.
"""
from algorithms.dp import get_maximum_value,Item

capacity = 5
#items = [[60, 5], [50, 3], [70, 4], [30, 2]] #(value, weight)
items=[Item(60,5),Item(50,3),Item(70,4),Item(30,2)]

print(get_maximum_value(items,capacity))