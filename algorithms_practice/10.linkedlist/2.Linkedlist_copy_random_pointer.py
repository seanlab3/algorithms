"""
A linked list is given such that each node contains an additional random
pointer which could point to any node in the list or null.
Return a deep copy of the list.
"""

# // Init a singly linked list [1,2,3].
# # ListNode head = new ListNode(1);
# # head.next = new ListNode(2);
# # head.next.next = new ListNode(3);

### XXX


from algorithms.linkedlist import RandomListNode,copy_random_pointer_v1,copy_random_pointer_v2

Linkedlist1=RandomListNode(1)
Linkedlist1.next=RandomListNode(2)
Linkedlist1.next=RandomListNode(3)

copy_random_pointer_v1(Linkedlist1)


copy_random_pointer_v2(Linkedlist1)