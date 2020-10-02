"""
Given a linked list, is_sort function returns true if the list is in sorted
(increasing) order and return false otherwise. An empty list is considered
to be sorted.
For example:
Null :List is sorted
1 2 3 4 :List is sorted
1 2 -1 3 :List is not sorted
"""
from algorithms.linkedlist import is_sorted
class Node(object):
    def __init__(self, x):
        self.val = x
        self.next = None
def print_linked_list(head):
    string = ""
    while head.next:
        string += head.val + " -> "
        head = head.next
    string += head.val
    print(string)


node1=Node(1)
node2=Node(2)
node3=Node(3)
node4=Node(4)
node1.next=node2
node2.next=node3
node3.next=node4


node5=Node(1)
node6=Node(2)
node7=Node(-1)
node8=Node(3)
node5.next=node6
node6.next=node7
node7.next=node8


print(is_sorted(node1))


print(is_sorted(node5))

