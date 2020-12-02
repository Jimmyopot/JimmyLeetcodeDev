# soln 1

class ListNode(object):
    def __init__(self, x):
        self.val = x 
        self.next = None
        
class Solution(ListNode):
    def mergeTwoLists(self, l1, l2):
        head = ListNode(0)
        pointer = head
        
        while True:
            if l1 is None and l2 is None:
                break
            elif l1 is None:
                pointer.next = l2
                break
            elif l2 is None:
                pointer.next = l1
                break
            else:
                smallerVal = 0
                if l1.val < l2.val:
                    smallerVal = l1.val
                else:
                    smallerVal = l2.val
                    l2 = l2.next 
                newNode = ListNode(smallerVal)
                pointer.next = newNode
                pointer = pointer.next 
                
        return head.next
    
l = Solution()
print(l.mergeTwoLists([1,2,4], [1,3,4]))



# soln 2

class Node:
        def __init__(self, data):
            self.data = data
            self.next = None
            
class LinkedList:
    def __init__(self):
        self.head = None

class Solution2(object):       
    def mergeTwoLists2(self, l1, l2):
        p = self.head  # points to head of 1st linked list
        q = self.head  # points to head of 2nd linked list
        s = None  # this pointer points to the list node btw p and q
        
        if not p:
            return q
        if not q:
            return p
        
        if p and q:
            if p.data <= q.data:
                s = p
                p = s.next 
            else:
                s = q
                q = s.next
            new_head = s
            
        while p and q:
            if p.data <= q.data:
                s.next = p
                s = p
                p = s.next
            else:
                s.next = q
                s = q
                q = s.next
                
        if not p:
            s.next = q
        if not q:
            s.next = p
    
        return new_head
    
l = Solution2()
print(l.mergeTwoLists2([1,2,4], [1,3,4]))



# soln 3   *************************ACCEPTED*****************************
'''
- But not working on vsCode terminal
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val 
        self.next = next 
        
class Solution3(ListNode):       
    def mergeTwoLists3(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        
        if l1.val <= l2.val:
            head = l1
            head.next = self.mergeTwoLists3(l1.next, l2)
        else:
            head = l2
            head.next = self.mergeTwoLists3(l1, l2.next)
            
        return head
    
l = Solution3()
print(l.mergeTwoLists3([1,2,4], [1,3,4]))



# soln 4

class ListNode(object):
    def __init__(self, x):
        self.val = x 
        self.next = None
        
class Solution4:
    def mergeTwoLists4(self, l1: ListNode, l2: ListNode) -> ListNode:
        # '''
        # time complexity O(n) and space complexity O(1)
        # '''
        temp = dummy = ListNode(0)  # create dummy node
        
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        
        while l1 and l2:
            if l1.val < l2.val:
                temp.next = l1
                l1 = l1.next
            else:
                temp.next = l2
                l2 = l2.next
                
        if l1:
            temp.next = l1
        if l2:
            temp.next = l2
        return dummy.next
        
l = Solution4()
print(l.mergeTwoLists4([1,2,4], [1,3,4]))