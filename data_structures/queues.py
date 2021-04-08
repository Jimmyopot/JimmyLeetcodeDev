'''
- A Queue is a data structure that stores items in an First-In/First-Out manner(FIFO).
- There are two types of operations in Queue-
    Enqueue – To add new items at the back.
    Dequeue - To remove items at the front. (popleft())
- Time Complexity : O(1)
'''

# Example 1

class Queue:
    def __init__(self):
        self.items = []
        
    def isEmpty(self):
        return self.items == []
    
    def enqueue(self, item):
        self.items.insert(0, item)
        
    def dequeue(self):
        return self.items.pop()
    
    def size(self):
        return len(self.items)
       
q = Queue()

q.enqueue(4)
q.enqueue("cat")
q.enqueue(True)
print(q.dequeue())
print(q.size())



# example 2

class Queue2:
    
  def __init__(self):
      self.queue = list()

  def addtoq(self,dataval):
# Insert method to add element
      if dataval not in self.queue:
          self.queue.insert(0,dataval)
          return True
      return False
# Pop method to remove element
  def removefromq(self):
      if len(self.queue)>0:
          return self.queue.pop()
      return ("No elements in Queue!")

TheQueue = Queue2()
TheQueue.addtoq("Mon")
TheQueue.addtoq("Tue")
TheQueue.addtoq("Wed")
print(TheQueue)
print(TheQueue.removefromq())
print(TheQueue.removefromq())