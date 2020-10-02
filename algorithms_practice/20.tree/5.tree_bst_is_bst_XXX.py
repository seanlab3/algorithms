"""
Given a binary tree, determine if it is a valid binary search tree (BST).
Assume a BST is defined as follows:
The left subtree of a node contains only nodes
with keys less than the node's key.
The right subtree of a node contains only nodes
with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
Example 1:
    2
   / \
  1   3
Binary tree [2,1,3], return true.
Example 2:
    1
   / \
  2   3
Binary tree [1,2,3], return false.
"""
from algorithms.tree.bst import is_bst
class TreeNode:

    # Constructor to create a new node
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None

root  = TreeNode(1)

# Creating the tree given in the above diagram
root.left = TreeNode(2)
# root.left.left=TreeNode(2)
# root.left.right=TreeNode(4)

root.right = TreeNode(3)
# root.right.right=TreeNode(7)

print(is_bst(root))