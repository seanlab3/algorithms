"""
Given a linked list, determine if it has a cycle in it.
Follow up:
Can you solve it without using extra space?
"""

from algorithms.linkedlist.is_cyclic import Node,is_cyclic

node1=Node(1)
node1.next=Node(2)
node1.next.next=Node(3)

print(is_cyclic(node1))

