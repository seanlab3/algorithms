from algorithms.tree.red_black_tree.red_black_tree import RBNode,RBTree


rb = RBTree()
children = [11, 2, 14, 1, 7, 15, 5, 8, 4]
for child in children:
    node = RBNode(child, 1)
    print(child)
    rb.insert(node)
print(rb.inorder())