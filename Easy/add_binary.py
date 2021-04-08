"""
HOW BINARY SYSTEM WORKS:

- Each position in a num rep a certain value/binary.
- For every num, the position rep BASE 10, eg. 237

2 1 0 -> power of....
2 3 7
(10^2 * 2) + (10^1 * 3) + (10^0 * 7) = 237
    200           30            7
    
    
- For binary digits, the position rep BASE 2, eg. 111

4 2 1 -> power of....
1 1 1
(1 * 1) + (2 * 1) + (4 * 1) = 7
   1         2         4
   
1 0 1 1 1 0 1 1
(1 * 1) + (2 * 1) + (4 * 0) + (8 * 1) + (16 * 1) + (32 * 1) + (64 * 0) + (128 * 1) = 187

"""

# soln 1

class Solution(object):
    def addBinary(self, a, b):
        result = ""
        i = len(a) - 1
        j = len(b) - 1
        carry = 0
        
        while i >= 0 or j >= 0:
            sum = carry
            if i >= 0:
                sum += ord(a[i]) - ord('0')
            if j >= 0:
                sum += ord(b[j]) - ord('0')
            i = i - 1
            j = j - 1
            if sum > 1:
                carry = 1
            else:
                0
            result += str(sum % 2)
            
        if carry != 0:
            result += str(carry)
        return result [::-1]
    
l = Solution()
print(l.addBinary("11", "1"))



# soln 4 ************BEST SOLN**************

class Solution4(object):
    def addBinary4(self, a, b):
        i = len(a) - 1
        j = len(b) - 1
        carry = 0
        result = ""
        
        # WHILE LOOP -> greater than, decrement....less than, increment
        while i >= 0 or j >= 0:
            sum = carry
            if i >= 0:
                sum += int(a[i])
                i -= 1  # decrement to avoid an infinite loop
            if j >= 0:
                sum += int(b[j])
                j -= 1  # decrement to avoid an infinite loop
            
            result = str(sum % 2) + result  # mode 2 (% 2) always returns a 0 if even an 1 if odd
            # 0 % 2 = 0 , 1 % 2 = 1 , 2 % 2 = 0 , 3 % 2 = 1
            carry = sum // 2  # this is FLOOR, returns whole no.
            
        if carry == 1:
            result = '1' + result
        return result
    
l = Solution4()
print(l.addBinary4("11", "1"))



# soln 2

class Solution2(object):
    def addBinary2(self, a, b):
        i = len(a) - 1
        j = len(b) - 1
        carry = 0
        output = ''
        
        while i != -1 or j != -1 or carry:
            if i != -1:
                carry += int(a[i])
                i -= 1
            if j != -1:
                carry += int(b[j])
                j -= 1
            output = str(carry & 1) + output
            carry >>=1
        return output
    
l = Solution2()
print(l.addBinary2("1010", "1011"))



# soln 3 [Michelle Chinese soln]

class Solution3(object):
    def addBinary3(self, a, b):
        result = ""
        carry = 0
        val = 0
        
        for i in range(max(len(a), len(b))):
            val = carry
            if i < len(a):
                val += int(a[-(i+1)])
            if i < len(b):
                val += int(b[-(i+1)])
            carry = val // 2
            val = val % 2
            result += str(val)
        if carry:
            result += str(1)
        return result[::-1]
    
l = Solution3()
print(l.addBinary3("1010", "1011"))
