"""
Queue Abstract Data Type (ADT)
* Queue() creates a new queue that is empty.
  It needs no parameters and returns an empty queue.
* enqueue(item) adds a new item to the rear of the queue.
  It needs the item and returns nothing.
* dequeue() removes the front item from the queue.
  It needs no parameters and returns the item. The queue is modified.
* isEmpty() tests to see whether the queue is empty.
  It needs no parameters and returns a boolean value.
* size() returns the number of items in the queue.
  It needs no parameters and returns an integer.
* peek() returns the front element of the queue.
"""

from algorithms.queues import QueueNode,LinkedListQueue


myQueue = LinkedListQueue()

myQueue.enqueue(5)
myQueue.enqueue(6)
myQueue.enqueue(9)
myQueue.enqueue(5)
myQueue.enqueue(3)
print(myQueue.peek())
print(myQueue.dequeue())  #prints 5
print(myQueue.dequeue())  #prints 6
print(myQueue.dequeue())  #prints 9
print(myQueue.dequeue())  #prints 3
print(myQueue.peek())     #prints 0
print(myQueue.dequeue())
#print(myQueue.dequeue())