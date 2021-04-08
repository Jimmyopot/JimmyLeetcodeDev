'''
- A linked list is a sequence of data elements, which are connected together via links. 
- Each data element contains a connection to another data element in form of a POINTER.
'''

# CREATING A LINKED LIST

class Node:
    def __init__(self, dataval = None):
        self.dataval = dataval
        self.nextval = None
        
class SLinkedList:
    def __init__(self):
        self.headval = None
        
list1 = SLinkedList()
list1.headval = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")
# Link 1st node to 2nd node
list1.headval.nextval = e2
# Link 2nd node to 3rd node
e2.nextval = e3



# TRAVERSING A LINKED LIST

class Node2:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None
        
class SlinkedList2:
    def __init__(self):
        self.headval = None
    
    # Print the Linked List  
    def listprint(self):
        printval = self.headval
        
        while  printval is not None:
            print(printval.dataval)
            printval = printval.nextval
            
list = SlinkedList2()
list.headval = Node2("Thur")
e2 = Node2("Fri")
e3 = Node2("Sat")

# Link 1st node to 2nd node
list.headval.nextval = e2

# Link 2nd node to 3rd node 
e2.nextval = e3

list.listprint()
print("*****************")



# INSERTION
# a) Inserting at the beginning of the Linked List

class Node3:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None
        
class SlinkedList3:
    def __init__(self):
        self.headval = None
    
    # Print the Linked List  
    def listprint3(self):
        printval = self.headval
        
        while  printval is not None:
            print(printval.dataval)
            printval = printval.nextval
            
    def AtBeginning(self, newdata):
        NewNode = Node3(newdata)
        # Update the new nodes next val to existing node
        NewNode.nextval = self.headval
        self.headval = NewNode
        
list3 = SlinkedList3()
list3.headval = Node3("Mon")
e2 = Node3("Tue")
e3 = Node3("Wed")

list3.headval.nextval = e2
e2.nextval = e3

list3.AtBeginning("Sun")
list3.listprint3()
print("*****************")




# a) Inserting at the end of the Linked List

class Node4:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None
        
class SlinkedList4:
    def __init__(self):
        self.headval = None
        
    # Function to add new node
    def AtEnd(self, newdata):
        NewNode = Node4(newdata)
        if self.headval is None:
            self.headval = NewNode
            return
        laste = self.headval
        
        while(laste.nextval):
            laste = laste.nextval
        laste.nextval = NewNode
            
    # Print the Linked List  
    def listprint4(self):
        printval = self.headval
        
        while  printval is not None:
            print(printval.dataval)
            printval = printval.nextval
            
list4 = SlinkedList4()
list4.headval = Node4("Mon")
e2 = Node4("Tue")
e3 = Node4("Wed")

list4.headval.nextval = e2
e2.nextval = e3

list4.AtEnd("Thur")
list4.listprint4()
print("*****************")



# a) Removing at the end of the Linked List

class Node5:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        
class SlinkedList5:
    def __init__(self):
        self.head = None
        
    def Atbeginning(self, data_in):
        NewNode = Node5(data_in)
        NewNode.next = self.head
        self.head = NewNode
        
    # Function to remove new node
    def RemoveNode(self, RemoveKey):
        HeadVal = self.head
        if HeadVal.data == RemoveKey:
            self.head = HeadVal.next
            HeadVal = None
            return 
        
        while HeadVal is not None:
            if HeadVal.data == RemoveKey:
                break
            prev = HeadVal
            HeadVal = HeadVal.next
            
        if HeadVal == None:
            return
        
        prev.next = HeadVal.next
        HeadVal = None 
            
    # Print the Linked List  
    def listprint5(self):
        printval = self.head
        
        while printval:
            print(printval.data)
            printval = printval.next
            
llist5 = SlinkedList5()
llist5.Atbeginning("Mon")
llist5.Atbeginning("Tue")
llist5.Atbeginning("Wed")
llist5.Atbeginning("Thu")
llist5.RemoveNode("Tue")
llist5.listprint5()
print("*****************")



# Example from TREE HOUSE code
class Node6:
    """
    An object for storing a single node of a linked list.
    models 2 attributes - data and the link to the next node in the list
    """
    
    data = None
    next_node = None
    
    def __init__(self, data):
        self.data = data
        
    def __repr__(self):
        return "<Node data: %s>" % self.data
    
    
class LinkedList:
    """
    Singly linked list
    """
    def __init__(self):
        self.head = None
        
    def is_empty(self):
        return self.head == None
    
    def size(self):
        """
        Returns the no. of nodes in list
        Takes O(n) time-> linear time
        """
        current = self.head 
        count = 0
        
        while current:
            count += 1
            current = current.next_node
            
        return count
    
    def add(self, data):
        """
        Adds new node containing data as head of list
        Takes O(1) time-> constant time
        """
        new_node = Node6(data)
        new_node.next_node = self.head 
        self.head = new_node
        
    def search(self, key):
        """
        Search for the 1st node containing data that matches the key
        Return the node or None if not fount
        Takes O(n) time
        """
        current = self.head
        
        while current:
            if current.data == key:
                return current
            else:
                current = current.next_node
            return None
        
    def insert(self, data, index):
        """
        Inserts a new node containing data at index position
        Inserting takes O(1) time
        Searching for inserted node takes O(n) time
        """
        if index == 0:
            self.add(data)
        if index > 0:
            new = Node6(data)
        
        position = index
        current = self.head
        
        while position > 1:
            current = new.next_node
            position -= 1
            
        prev_node = current
        next_node = current.next_node
        
        prev_node.next_node = new
        new.next_node = next_node
        
    def remove(self, key):
        current = self.head
        previous = None
        found = False
        
        while current and not found:
            if current.data == key and current is self.head:
                found = True
                self.head = current.next_node
            elif current.data == key:
                found = True
                previous.next_node = current.next_node
            else:
                previous = current
                current = current.next_node
        
    def __repr__(self):
        """
        Returns a string representation of the list
        Takes O(n) time
        """
        
        nodes = []
        current = self.head    
        
        while current:
            if current is self.head:
                nodes.append("[Head: %s]" % current.data)
            elif current.next_node is None:
                nodes.append("[Tail: %s]" % current.data)
            else:
                nodes.append("[%s]" % current.data)
                
            current = current.next_node
        return '-> '.join(nodes)