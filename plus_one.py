# soln 1

class Solution(object):
    def plusOne(self, digits):
        idx = len(digits) - 1  # last digit in array  [1, 9, 9, 9]
        
        while idx >= 0:
            if digits[idx] == 9:
                digits[idx] = 0  # [1, 9, 9, 9] = [2, 0, 0, 0]
            else:
                digits[idx] += 1
                return digits
            idx -= 1
            
        return [1] + digits
    
l = Solution()
print(l.plusOne([1, 9, 9, 9]))



# soln 2

class Solution2(object):
    def plusOne2(self, digits):
        n = len(digits)
        
        for i in range(n-1, -1, -1):  # means counting from the end to start of list
            if digits[i] < 9:
                digits[i] += 1
                return digits
            else:
                digits[i] = 0  # this means if digits is 9 return 0   [1,9,9,9] = [2,0,0,0]
                
        digits.insert(0, 1)  # this means insert 1 at the first(0) element
        return digits
    
l = Solution2()
print(l.plusOne2([1, 9, 9, 9]))



# soln 3 [Chinese Michelle soln] **************BEST SOLN************

class Solution3(object):
    def plusOne3(self, digits):
        for i in reversed(range(len(digits))):  # this means we start from the end of the list to the first(reversed)
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                return digits
        ''' 
        digits[0] = 1  # first element = 1 [1]
        digits.append(0)  # add 0 [1, 0]
        return digits
        '''
        digits.insert(0, 1)  # this means insert 1 at the first(0) element
        return digits
    
l = Solution3()
print(l.plusOne3([9, 9, 9]))
        
            