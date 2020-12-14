# soln 1

class Solution(object):
    def isValid(self, s):
        '''
        - build a stack.
        - pop the parenthesis.
        '''
        stack = []
        lookup = {
            ")":"(", "}":"{", "]":"["
        }
        
        for parenthesis in s:
            if parenthesis in lookup.values():
                stack.append(parenthesis)
            elif stack and lookup[parenthesis] == stack[-1]:
                stack.pop()
            else:
                return False
            
        return stack == []
    
l = Solution()
print(l.isValid("{[]}"))



# soln 2

class Solution2(object):
    def isValid2(self, s):
        pastParens = []  # list used to check parentheses (used as STACK)
        
        for i in range(len(s)):
            if self.isOpenParen(s[i]):  # function is below
                pastParens.append(s[i])
            else:
                if len(pastParens) == 0:
                    return False
                op = pastParens.pop()
                cl = s[i]
                isValid = self.parenIsSameType(op, cl)  # function is below
                if not isValid:
                    return False
        return len(pastParens) == 0
    
    def isOpenParen(self, p):
        if p == '{' or p == '[' or p == '(':
            return True
        return False
    
    def parenIsSameType(self, op, cl):
        if op == '(' and cl == ')':
            return True
        elif op == '[' and cl == ']':
            return True
        elif op == '{' and cl == '}':
            return True
        else:
            return False
        
l = Solution2()
print(l.isValid2("{{[]}]"))



# soln 3

class Solution3(object):
    def isValid3(self, s):
        stack = Stack()
        
        opening = "([{"
        closing = ")]}"
        
        if s == "":
            return True
        if len(s) < 2:
            return False
        
        for i in s:
            if i in closing and not stack.is_empty():
                popped = stack.pop()
                closing_index = closing.index(i)
                opening_index = opening.index(popped)
                if opening_index != closing_index:
                    return False
            else:
                stack.push(i)
        if stack.is_empty():
            return True
        return False
    
    
class Stack:
    def __init__(self):
        self.stack = []
        
    def is_empty(self):
        return len(self.stack) == 0
    
    def push(self, item):
        self.stack.append(item)
        
    def pop(self):
        return self.stack.pop()
    
    def peek(self):
        return self.stack[len(self.stack) -1]
 
l = Solution3()
print(l.isValid3("({[]})"))      



# soln 4

'''
- initialize a stack s.
- iterate over each character in the string.
- if we encounter an open bracket, push it onto the stack.
- if we encounter a closing bracket, check top of the stack.
    a. if top of stack is an open bracket of the same type, continue
    b. else, return false
'''

class Solution4(object):
    def isValid4(self, s):
        
        stack = []
        mapping = {")":"(", "}":"{", "]":"["} 
        
        for char in s:
            if char in mapping:
                if stack:
                    top_elem = stack.pop()
                else:
                    top_elem = ""
                    
                if mapping[char] != top_elem:
                    return False
            else:
                stack.append(char)
        return not stack
                    
l = Solution4()
print(l.isValid4("({[]})"))
# runtime = O(n)
# space = O(n)
        