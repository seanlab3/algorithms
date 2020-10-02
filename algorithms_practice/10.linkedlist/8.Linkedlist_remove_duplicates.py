from algorithms.linkedlist.remove_duplicates import  Node,print_linked_list,remove_dups,remove_dups_wothout_set

# A A B C D C F G

a1 = Node("A")
a2 = Node("A")
b = Node("B")
c1 = Node("C")
d = Node("D")
c2 = Node("C")
f = Node("F")
g = Node("G")

a1.next = a2
a2.next = b
b.next = c1
c1.next = d
d.next = c2
c2.next = f
f.next = g

remove_dups(a1)
print_linked_list(a1)
remove_dups_wothout_set(a1)
print_linked_list(a1)