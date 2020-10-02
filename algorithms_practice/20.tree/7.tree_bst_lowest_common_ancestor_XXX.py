"""
Given a binary search tree (BST),
find the lowest common ancestor (LCA) of two given nodes in the BST.
According to the definition of LCA on Wikipedia:
    “The lowest common ancestor is defined between two
    nodes v and w as the lowest node in T that has both v and w
    as descendants (where we allow a node to be a descendant of itself).”
        _______6______
       /              \
    ___2__          ___8__
   /      \        /      \
   0      _4       7       9
         /  \
         3   5
For example, the lowest common ancestor (LCA) of nodes 2 and 8 is 6.
Another example is LCA of nodes 2 and 4 is 2,
since a node can be a descendant of itself according to the LCA definition.
"""

from algorithms.tree.bst.lowest_common_ancestor import lowest_common_ancestor

class Node:

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


n1 = Node(6)
n2 = Node(2)
n3 = Node(8)

n4 = Node(0)
n5 = Node(4)
n6 = Node(3)
n7 = Node(5)

n8 = Node(7)
n9 = Node(9)


n1.left, n1.right = n2, n3
n2.left, n2.right = n4, n5
n5.left, n5.right = n6, n7
n3.left, n3.right = n8, n9

print(lowest_common_ancestor(n1,n2,n3))