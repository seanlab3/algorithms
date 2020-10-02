"""
Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.
Basically, the deletion can be divided into two stages:
Search for a node to remove.
If the node is found, delete the node.
Note: Time complexity should be O(height of tree).
Example:
root = [5,3,6,2,4,null,7]
key = 3
    5
   / \
  3   6
 / \   \
2   4   7
Given key to delete is 3. So we find the node with value 3 and delete it.
One valid answer is [5,4,6,2,null,null,7], shown in the following BST.
    5
   / \
  4   6
 /     \
2       7
Another valid answer is [5,2,6,null,4,null,7].
    5
   / \
  2   6
   \   \
    4   7
"""
from algorithms.tree.bst.delete_node import Solution
from algorithms.tree.bst.BSTIterator  import BSTIterator



class TreeNode:

    # Constructor to create a new node
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None


root  = TreeNode(5)

# Creating the tree given in the above diagram
root.left = TreeNode(3)
root.left.left=TreeNode(2)
root.left.right=TreeNode(4)

root.right = TreeNode(6)
root.right.right=TreeNode(7)



a=Solution()
b=a.delete_node(root,3)

biter=BSTIterator(b)
while biter.has_next():
    print(biter.next())
