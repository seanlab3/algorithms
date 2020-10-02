from algorithms.tree.bst.predecessor import predecessor
from algorithms.tree.bst.BSTIterator  import BSTIterator

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

b=predecessor(n1,n2)

biter=BSTIterator(b)
while biter.has_next():
    print(biter.next())