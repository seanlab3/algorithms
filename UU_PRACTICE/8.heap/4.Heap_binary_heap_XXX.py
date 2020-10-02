"""
Binary Heap. A min heap is a complete binary tree where each node is smaller
its childen. The root, therefore, is the minimum element in the tree. The min
heap use array to represent the data and operation. For example a min heap:
     4
   /   \
  50    7
 / \   /
55 90 87
Heap [0, 4, 50, 7, 55, 90, 87]
Method in class: insert, remove_min
For example insert(2) in a min heap:
     4                     4                     2
   /   \                 /   \                 /   \
  50    7      -->     50     2       -->     50    4
 / \   /  \           /  \   / \             /  \  /  \
55 90 87   2         55  90 87  7           55  90 87  7
For example remove_min() in a min heap:
     4                     87                    7
   /   \                 /   \                 /   \
  50    7      -->     50     7       -->     50    87
 / \   /              /  \                   /  \
55 90 87             55  90                 55  90
"""
from algorithms.heap import binary_heap,AbstractHeap

a=[0, 4, 50, 7, 55, 90, 87]

heapObj = AbstractHeap()
heapObj.insertKey(0)
heapObj.insertKey(4)
heapObj.insertKey(50)
heapObj.insertKey(7)
heapObj.insertKey(55)
heapObj.insertKey(90)
heapObj.insertKey(87)