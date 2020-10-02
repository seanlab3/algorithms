"""
Reverse a singly linked list. For example:
1 --> 2 --> 3 --> 4
After reverse:
4 --> 3 --> 2 --> 1
"""
from algorithms.linkedlist import Node,reverse_list,reverse_list_recursive

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


print_linked_list(reverse_list(node1))

print_linked_list(reverse_list_recursive(node1))