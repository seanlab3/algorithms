# Given a non-empty binary search tree and a target value,
# find the value in the BST that is closest to the target.

# Note:
# Given target value is a floating point.
# You are guaranteed to have only one unique value in the BST
# that is closest to the target.


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from algorithms.tree.bst.bst_closest_value import closest_value
from algorithms.tree.bst.array_to_bst import TreeNode,array_to_bst

a=[2,56,34,25,13,2,3,5,7,10]

b=array_to_bst(a)

print(closest_value(b, 15))

