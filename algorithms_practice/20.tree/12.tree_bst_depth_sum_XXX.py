"""
Write a function depthSum returns the sum of the values stored
in a binary search tree of integers weighted by the depth of each value.
For example:
                    9
                 /      \
               6         12
              / \       /   \
            3     8   10      15
                 /              \
                7                18
    depth_sum = 1*9 + 2*(6+12) + 3*(3+8+10+15) + 4*(7+18)
"""

from algorithms.tree.bst.depth_sum import depth_sum,recur_depth_sum
from algorithms.tree.bst import bst
from algorithms.tree.bst import Node

tree = bst()
tree.insert(9)
tree.insert(6)
tree.insert(12)
tree.insert(3)
tree.insert(8)
tree.insert(10)
tree.insert(15)
tree.insert(7)
tree.insert(18)

print(depth_sum(tree.root, 4))

