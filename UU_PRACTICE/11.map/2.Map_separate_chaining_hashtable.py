from algorithms.map import Node,SeparateChainingHashTable

node1=Node(1,35)
node1.next=Node(2,45)
node1.next.next=Node(3,33)


schash=SeparateChainingHashTable()
schash.put(4,77)


##
print(schash.get(4))
schash.del_(4)
print(schash.get(4))
