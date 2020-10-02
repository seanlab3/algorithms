"""
    Given a linked list, find the first node of a cycle in it.
    1 -> 2 -> 3 -> 4 -> 5 -> 1  => 1
    A -> B -> C -> D -> E -> C  => C
    Note: The solution is a direct implementation
          Floyd's cycle-finding algorithm (Floyd's Tortoise and Hare).
"""

from algorithms.linkedlist.first_cyclic_node import Node,first_cyclic_node,TestSuite

test=TestSuite()
test.test_first_cyclic_node()