'''
- Tree represents the nodes connected by edges. 
- It is a non-linear data structure.
- It has the following properties.
    # One node is marked as Root node.
    # Every node other than the root is associated with one parent node.
    # Each node can have an arbiatry number of chid node.
    
- Search for a value in a Binary tree:
  # Searching for a value in a tree involves comparing the incoming value with the value exiting nodes. 
  # Here also we traverse the nodes from left to right and then finally with the parent. 
  # If the searched for value does not match any of the exitign value, then we return not found message else the found message is returned.
'''

# creating root node

class Node:
    def __init__(self, data):
        self.left = None  # Left Child
        self.right = None  # Right Child
        self.data = data  # Node Data 
        
    # inserting into a tree
    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
                    
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
                    
        else:
            self.data = data 
            
    # search for value in a binary tree.
    # findval method to compare the value with nodes
    def findval(self, search_val):
        if search_val < self.data: 
            if self.left is None:
                return str(search_val) + " Not Found"
            return self.left.findval(search_val)
        elif search_val > self.data:
            if self.right is None:
                return str(search_val) + " Not Found"
            return self.right.findval(search_val)
        else:
            print(str(self.data) + " Found!")
       
    # function to print tree
    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.data),
        if self.right:
            self.right.printTree()
        

root = Node(12)
root.insert(6)
root.insert(14)
root.insert(16)
root.insert(3)

root.printTree()

print(root.findval(1))
print(root.findval(14))