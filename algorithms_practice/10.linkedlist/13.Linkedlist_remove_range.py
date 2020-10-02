"""
Given a linked list, remove_range function accepts a starting and ending index
as parameters and removes the elements at those indexes (inclusive) from the list
For example:
List: [8, 13, 17, 4, 9, 12, 98, 41, 7, 23, 0, 92]
remove_range(list, 3, 8);
List becomes: [8, 13, 17, 23, 0, 92]
legal range of the list (0 < start index < end index < size of list).
"""
from algorithms.linkedlist import remove_range

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

number1 = Node("8")
number1.next = Node("13")
number1.next.next = Node("17")
number1.next.next.next = Node("4")
number1.next.next.next.next = Node("9")
number1.next.next.next.next.next = Node("12")
number1.next.next.next.next.next.next = Node("98")
number1.next.next.next.next.next.next.next = Node("41")
number1.next.next.next.next.next.next.next.next = Node("7")
number1.next.next.next.next.next.next.next.next.next = Node("23")
number1.next.next.next.next.next.next.next.next.next.next = Node("0")
number1.next.next.next.next.next.next.next.next.next.next.next = Node("92")

print_linked_list(remove_range(number1,3,8))