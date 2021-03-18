'''
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

For example, 2 is written as II in Roman numeral, just two one's added together. 
12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. 
However, the numeral for four is not IIII. Instead, the number four is written as IV. 
Because the one is before the five we subtract it making four. The same principle applies 
to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.
'''


# soln 1  *****************************BEST SOLN****************************************

class Solution(object):
    def romanToInt(self, s):
        
        dic = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        
        current = 0
        previous = 0
        total = 0
        
        for i in range(len(s)):
            current = dic[s[i]]
            if current > previous:
                '''
                XLIX:
                10+50-2(10)+1+10-2(1)=49
                XVIX:
                10+5+1+10-2(1)=24
                '''
                total = total + current - 2 * previous
            else:
                total += current
                
            previous = current
        return total
    
l = Solution()
print(l.romanToInt("XXCDM"))



# soln 2

# s = "XCV"
class Solution1(object):
    def romanToInt1(self, s):
        
        d = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        ans = 0

        for i in range(len(s)):
            if i+1 != len(s) and d[s[i]] < d[s[i+1]]:
                ans = ans - d[s[i]]
            else:
                ans = ans + d[s[i]]
        return ans
        # 10+100-2(10)+5=95
    
l = Solution1()
print(l.romanToInt1("XCV"))



# soln 3

class Solution2(object):
    def romanToInt2(self, s):
        
        mapping = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        
        number = mapping[s[-1]]  # starts from the last character in the dictionary, if its greater than current
        
        for i in reversed(range(len(s)-1)):  # we are looping from the end
            if mapping[s[i+1]] > mapping[s[i]]:  # if number is greater than previous number, subtract
                number -= mapping[s[i]]
            else:
                number += mapping[s[i]]
        return number
    
l = Solution2()
print(l.romanToInt2("XVIX"))

