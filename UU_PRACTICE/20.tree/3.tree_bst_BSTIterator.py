
from algorithms.tree.bst.BSTIterator  import BSTIterator

class TreeNode:

    # Constructor to create a new node
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None

root  = TreeNode(20)

# Creating the tree given in the above diagram
root.left = TreeNode(8)
root.left.left=TreeNode(4)
root.left.right=TreeNode(12)
root.left.right.left=TreeNode(10)
root.left.right.right=TreeNode(14)

root.right=TreeNode(22)

biter=BSTIterator(root)
while biter.has_next():
    print(biter.next())


