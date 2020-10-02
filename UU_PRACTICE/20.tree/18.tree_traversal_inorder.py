from algorithms.tree.traversal import Node,inorder,inorder_rec

n1 = Node(100)
n2 = Node(50)
n3 = Node(150)
n4 = Node(25)
n5 = Node(75)
n6 = Node(125)
n7 = Node(175)
n1.left, n1.right = n2, n3
n2.left, n2.right = n4, n5
n3.left, n3.right = n6, n7


print(inorder(n1))
print(inorder_rec(n1))
# assert inorder(n1)     == [25, 50, 75, 100, 125, 150, 175]
# assert inorder_rec(n1) == [25, 50, 75, 100, 125, 150, 175]