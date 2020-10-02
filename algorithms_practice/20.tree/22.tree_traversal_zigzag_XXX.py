from algorithms.tree.traversal.zigzag import zigzag_level

class TreeNode:

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

n1 = TreeNode(6)
n2 = TreeNode(2)
n3 = TreeNode(8)

n4 = TreeNode(0)
n5 = TreeNode(4)
n6 = TreeNode(3)
n7 = TreeNode(5)

n8 = TreeNode(7)
n9 = TreeNode(9)


n1.left, n1.right = n2, n3
n2.left, n2.right = n4, n5
n5.left, n5.right = n6, n7
n3.left, n3.right = n8, n9


print(zigzag_level(n1))