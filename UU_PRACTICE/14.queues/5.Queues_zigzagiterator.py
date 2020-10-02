

from algorithms.queues.zigzagiterator import ZigZagIterator


l1 = [1, 2]
l2 = [3, 4, 5, 6]
it = ZigZagIterator(l1, l2)
while it.has_next():
    print(it.next())
