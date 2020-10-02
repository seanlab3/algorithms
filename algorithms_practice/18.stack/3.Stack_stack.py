
from algorithms.stack.stack import StackNode,LinkedListStack

myStack = LinkedListStack()

myStack.push(5)
myStack.push(6)
myStack.push(9)
myStack.push(5)
myStack.push(3)
print(myStack.peek())
print(myStack.pop())  #prints 5
print(myStack.pop())  #prints 6
print(myStack.pop())  #prints 9
print(myStack.pop())  #prints 3
print(myStack.peek())     #prints 0
print(myStack.pop())