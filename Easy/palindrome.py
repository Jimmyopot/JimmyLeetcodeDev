# soln 1 (string convertion)

class Solution(object):
    def isPalindrome(self, x):
        return (str(x) == str(x)[::-1])
    
l = Solution()
print(l.isPalindrome(343))



# soln 2
y = 121 // 10 # this is floor function
print(y)

class Solution1(object):
    def isPalindrome1(self, x):
        if x < 0:
            return False
        
        reverse_num = 0
        digit = 0
        
        while(x // (10 ** digit) != 0):
            reverse_num = (reverse_num * 10) + (x // (10 ** digit) % 10)
            digit += 1
            
        return(x == reverse_num)
    
l = Solution1()
print(l.isPalindrome1(343))



# soln 3
'''
copy = 1234
b = 0
algorithm and calculations:
    
1234 % 10 = 4
1234 / 10 = 123
copy = 123
b = 0 * 10 + 4 = 4

123 % 10 = 3
123 / 10 = 12
copy = 12
b = 4 * 10 + 3 = 43
.....
'''

class Solution2(object):
    def isPalindrome2(self, x):
        if x < 0:
            return False 
        
        copy = x 
        b = 0
    
        # while copy:
        # while copy > 0:
        while True:
            copy /= 10
            b = b * 10 + copy % 10        
        return b == x
    
b = Solution2()
print(b.isPalindrome2(121))
# TIME COMPLEXITY O(n)
# SPACE COMPLEXITY O(1)



# soln 4

class Solution3(object):
    def isPalindrome3(self, x):
        if x < 0:
            return False
        
        reverse = 0
        
        while x > 0:
            reverse = (reverse * 10) + (x % 10)
            x = x // 10
        return reverse 
    
l = Solution3()
print(l.isPalindrome3(121))
