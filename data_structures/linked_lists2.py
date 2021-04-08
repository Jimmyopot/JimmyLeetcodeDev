
# initializes node class (node = data + next)
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        
# initializes the head
class LinkedList:
    def __init__(self):
        self.head = Node()
        
    # append node at beginning of linked list
    def append(self, data):
        new_node = Node(data)
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = new_node
        
    # append node at end of linked list
    def append_at_end(self, data):
        if self.head is None:  # has nothing
            self.head = Node(data, None)
            return
        else:
            cur = self.head
            while cur.next is not None:  # has something
                cur = cur.next
            cur.next = Node(data)
        
    # length of linked list
    def length(self):
        cur = self.head
        total = 0
        while cur.next is not None:
            total += 1
            cur = cur.next
        return total
    
    # prints linked list
    def display(self):
        elems = []
        cur_node = self.head 
        while cur_node.next is not None:
            cur_node = cur_node.next 
            elems.append(cur_node.data)
        print(elems)
        
    def get(self, index):
        if index >= self.length():
            print("ERROR: 'Get' Index out of range!")
            return None
        cur_idx = 0
        cur_node = self.head 
        while True:
            cur_node = cur_node.next
            if cur_idx == index:
                return cur_node.data
            cur_idx += 1
            
    # delete node
    def erase(self, index):
        if index >= self.length():
            print("ERROR: 'Erase' Index out of range!")
            return
        cur_idx = 0
        cur_node = self.head
        while True:
            last_node = cur_node
            cur_node = cur_node.next
            if cur_idx == index:
                last_node.next = cur_node.next
                return
            cur_idx += 1
        
        
my_list = LinkedList()
my_list.display()

my_list.append(0)
my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)
my_list.display()

print("element at 2nd index: %d" % my_list.get(2))

my_list.erase(0)
my_list.display()

my_list.append_at_end(45)
my_list.display()