'''
- A stack is a data structure that stores items in an Last-In/First-Out manner(LIFO).
- There are two types of operations in Stack-
    Push– To add data into the stack.
    Pop– To remove data from the stack.
- Example, the Undo feature in your editor.
'''

myStack = []

myStack.append('a')
myStack.append('b')
myStack.append('c')

print(myStack)
# ['a', 'b', 'c']

print(myStack.pop())
# 'c'
print(myStack.pop())
# 'b'
print(myStack.pop())
# 'a'



'''
- Deque provides an O(1) time complexity for append and pop. 
- List  provides O(n) time complexity. 
'''
from collections import deque
 
stack = deque()
 
stack.append('a')
stack.append('b')
stack.append('c')
 
print('Initial stack:')
print(stack)
 
print('\nElements poped from stack:')
print(stack.pop())
print(stack.pop())
print(stack.pop())



# Example 1

# Implement stack using a linked list.
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
        
class Stack:
    # initialize a stack
    def __init__(self):
        self.head = Node("head")
        self.size = 0
        
    # string rep of stack
    def __str__(self):
        cur = self.head.next 
        out = ""
        while cur:
            out += str(cur.value) + "->"
            cur = cur.next 
        return out[:-3]
    
    # get current size of stack
    def getSize(self):
        return self.size
    
    # check if stack is empty
    def isEmpty(self):
        return self.size == 0
    
    # get top item of the stack
    def peek(self):
        if self.isEmpty():
            raise Exception("Peeking from an empty stack")
        return self.head.next.value
    
    # push a value into a stack
    def push(self, value):
        node = Node(value)
        node.next = self.head.next
        self.head.next = node
        self.size += 1
        
    # remove a value from stack and return
    def pop(self):
        if self.isEmpty():
            raise Exception("Popping from an empty stack")
        remove = self.head.next 
        self.head.next = self.head.next.next 
        self.size -= 1
        return remove.value
    
    
# driver code
if __name__ == "__main__":
    stack = Stack()
    for i in range(1, 11):
        stack.push(i)
    print(f"Stack: {stack}")
    
    for _ in range(1, 6):
        remove = stack.pop()
        print(f"Pop: {remove}")
    print(f"Stack: {stack}")
    
    
    
# Example 2

# A simple class stack that only allows pop and push operations
class Stack2:

    def __init__(self):
        self.stack = []
    
    # 
    def pop(self):
        if len(self.stack) < 1:
            return None
        return self.stack.pop()
    
    # Push elements in last index 
    def push(self, item):
        self.stack.append(item)
        
    # Allows us to see last element
    def peek(self):
        if self.stack:
            return self.stack[-1]
        else:
            return None
    
    # Shows size of stack
    def size(self):
        if self.stack:
            return len(self.stack)
        else:
            return None
        
    # Check if stack is empty
    def isempty(self):
        if self.stack == []:
            return True
        else:
            return False
    
    
if __name__=="__main__":
    s = Stack2()
    s.push(1)
    s.push(2)
    s.push(3)
    print(s.size())
    print(s.peek())
    
    s.pop()
    print(s.size())
    print(s.peek())
    
# s = Stack2()

# # The first enters the title of the document
# print(s.push('mon'))
# # Next they center the text
# print(s.push('Tue'))
# # As with most writers, the user is unhappy with the first draft and undoes the center alignment
# print(s.pop())
# # The title is better on the left with bold font
# print(s.push('Wed'))