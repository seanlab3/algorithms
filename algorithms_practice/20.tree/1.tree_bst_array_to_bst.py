"""
Given an array where elements are sorted in ascending order,
convert it to a height balanced BST.
"""

from algorithms.tree.bst.array_to_bst import TreeNode,array_to_bst
COUNT = [2]
def print2DUtil(root, space) :

    # Base case
    if (root == None) :
        return

    # Increase distance between levels
    space += COUNT[0]

    # Process right child first
    print2DUtil(root.right, space)

    # Print current node after space
    # count
    print()
    for i in range(COUNT[0], space):
        print(end = " ")
    print(root.val)

    # Process left child
    print2DUtil(root.left, space)

# Wrapper over print2DUtil()
def print2D(root) :

    # space=[0]
    # Pass initial space count as 0
    print2DUtil(root, 0)

def Print(root, k1, k2):

    # Base Case
    if root is None:
        return

        # Since the desired o/p is sorted, recurse for left
    # subtree first. If root.data is greater than k1, then
    # only we can get o/p keys in left subtree
    if k1 < root.val  :
        Print(root.left, k1, k2)

        # If root's data lies in range, then prints root's data
    if k1 <= root.val  and k2 >= root.val :
        print(root.val )

        # If root.data is smaller than k2, then only we can get
    # o/p keys in right subtree
    if k2 > root.val :
        Print(root.right, k1, k2)


a=[i for i in range(1,11)]

b=array_to_bst(a)
print2D(b)

Print(b,1,10)




