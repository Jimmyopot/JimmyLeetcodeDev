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

# example 1

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
                    self.left.insert(data)  # recursion
                    
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



# example 2 [TREE TRAVERSAL]

class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        

class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)  # initializes root node
        
    def print_tree(self, traversal_type):
        if traversal_type == "preorder":
            return self.preorder_print(tree.root, "")
        elif traversal_type == "inorder":
            return self.inorder_print(tree.root, "")
        elif traversal_type == "postorder":
            return self.postorder_print(tree.root, "")
        else:
            print("Traversal type " + str(traversal_type) + " is not supported")
            return False
        
    # depth-first search / pre-order traversal
    def preorder_print(self, start, traversal):
        # Root -> left -> right
        if start:
            traversal += (str(start.value) + "_")
            traversal = self.preorder_print(start.left, traversal)  # remember this is RECURSION(calling func in itself)
            traversal = self.preorder_print(start.right, traversal)  # remember this is RECURSION(calling func in itself)
        return traversal
    
    # depth-first search / in-order traversal
    def inorder_print(self, start, traversal):
        # Left -> root -> right
        if start:
            traversal = self.inorder_print(start.left, traversal)  # remember this is RECURSION(calling func in itself)
            traversal += (str(start.value) + "_")
            traversal = self.inorder_print(start.right, traversal)  # remember this is RECURSION(calling func in itself)
        return traversal
    
    # depth-first search / post-order traversal
    def postorder_print(self, start, traversal):
        # Left -> right -> root
        if start:
            traversal = self.inorder_print(start.left, traversal)  # remember this is RECURSION(calling func in itself)
            traversal = self.inorder_print(start.right, traversal)  # remember this is RECURSION(calling func in itself)
            traversal += (str(start.value) + "_")
        return traversal
         
        
        
tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)                               #   1
tree.root.left.left = Node(4)                           # /   \
tree.root.left.right = Node(5)                          #2     3
tree.root.right.left = Node(6)                         #/ \   / \
tree.root.right.right = Node(7)                       #4   5 6   7
tree.root.right.right.right = Node(8)                #            \
                                                      #            8
print(tree.print_tree("preorder"))
# 1_2_4_5_3_6_7_8_
print(tree.print_tree("inorder"))
# 4_2_5_1_6_3_7_8_
print(tree.print_tree("postorder"))
# 4_2_5_6_3_7_8_1_




# example 3
# run time: log2(n)

class Node2:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
        
class binary_tree2:
    def __init__(self):
        self.root = None
        
    def add(self, current, value):
        if root is None:
            self.root = Node2(value)
        else:
            if value < current.value:
                if current.left == None:
                    current.left = Node2(value)
                else:
                    self.add(self.left, value)  # recursion            
            else:        
                if current.right == None:
                    current.right = Node2(value)
                else:
                    self.add(self.right, value)  # recursion
                                   
    def visit(self, node):
        print(node.value)
        
    # preorder search
    def preorder(self, current):
        # root -> left -> rigth
        self.visit(current)  # starts as root node
        self.preorder(current.left) #recursion
        self.preorder(current.rigth)  #recursion
        
    # inorder search
    def inorder(self, current):
        # left -> root -> rigth
        self.inorder(current.left) #recursion, starts as left node
        self.visit(current)  # root node
        self.inorder(current.rigth)  #recursion
        
    # postorder search
    def postorder(self, current):
        # left -> right -> root
        self.preorder(current.left) #recursion, starts as left node
        self.preorder(current.rigth)  #recursion
        self.visit(current)  # root node
    