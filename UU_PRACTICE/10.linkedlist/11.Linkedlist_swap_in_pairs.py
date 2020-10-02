"""
Given a linked list, swap every two adjacent nodes
and return its head.
For example,
Given 1->2->3->4, you should return the list as 2->1->4->3.
Your algorithm should use only constant space.
You may not modify the values in the list,
only nodes itself can be changed.
"""
from algorithms.linkedlist.swap_in_pairs import Node,swap_pairs
def print_linked_list(head):
    string = ""
    while head.next:
        string += head.val + " -> "
        head = head.next
    string += head.val
    print(string)

node1=Node("1")
node2=Node("2")
node3=Node("3")
node4=Node("4")
node1.next=node2
node2.next=node3
node3.next=node4

print_linked_list(swap_pairs(node1))


