"""
Given a list, rotate the list to the right by k places,
where k is non-negative.
For example:
Given 1->2->3->4->5->NULL and k = 2,
return 4->5->1->2->3->NULL.
"""
from algorithms.linkedlist import rotate_right
class ListNode(object):
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
node1=ListNode("1")
node2=ListNode("2")
node3=ListNode("3")
node4=ListNode("4")
node5=ListNode("5")
node1.next=node2
node2.next=node3
node3.next=node4
node4.next=node5
k=2
print_linked_list(rotate_right(node1,k))
