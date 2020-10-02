"""
I think my code's complexity is also O(nlogk) and not using heap or priority queue,
n means the total elements and k means the size of list.
The mergeTwoLists function in my code comes from the problem Merge Two Sorted Lists
whose complexity obviously is O(n), n is the sum of length of l1 and l2.
To put it simpler, assume the k is 2^x, So the progress of combination is like a full binary tree,
from bottom to top. So on every level of tree, the combination complexity is n,
because every level have all n numbers without repetition.
The level of tree is x, ie log k. So the complexity is O(n log k).
for example, 8 ListNode, and the length of every ListNode is x1, x2,
x3, x4, x5, x6, x7, x8, total is n.
on level 3: x1+x2, x3+x4, x5+x6, x7+x8 sum: n
on level 2: x1+x2+x3+x4, x5+x6+x7+x8 sum: n
on level 1: x1+x2+x3+x4+x5+x6+x7+x8 sum: n
"""

from algorithms.heap import merge_k_lists,ListNode


k=3
n=4

if __name__ == "__main__":
    a=[]

    list1=ListNode(1)
    list1.next=ListNode(4)
    list1.next.next=ListNode(5)
    a.append(list1)

    list2=ListNode(1)
    list2.next=ListNode(3)
    list2.next.next=ListNode(4)
    a.append(list2)


    list3=ListNode(2)
    list3.next=ListNode(6)
    a.append(list3)



    print(merge_k_lists(a))