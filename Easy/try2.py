def my_function(x):
      return x[::-1]

mytxt = my_function("I wonder how this text looks like backwards")

print(mytxt)

class Solution1:
    def reverse_int1(self, x):
        if x == int:
            return x[::-1]

s = Solution1()
print(s.reverse_int1(123))


class Solution(object):
    def reverse_int(self, x):
        y = str(abs(x))
        y = y.strip()
        y = y[::-1]
        output = int(y)
        return output
        
l = Solution()
print(l.reverse_int(123))
print(l.reverse_int(100987))
print(l.reverse_int(90000))


# palindrome example

class Solution2:
    def palindrome(self, x):
        x = str(abs(x))
        x = x[::-1]
        # x = int(x)
        if x == int(x):
            print("true")
        else:
            print("false")
            
l = Solution2()
print(l.palindrome(123)) 



class Solution3:
    def pal(self, x):
        if x < 0:
            return False
        
        reverse = 0
        
        while x > 0:
            reverse = (reverse * 10) + (x % 10)
            x = x // 10
        return reverse
    
l = Solution3()
print(l.pal(232))



# two sum review

class Solution4:
    def two_sum(self, nums, target):
        # nums -> array []
        # target -> int
        hash_map = {}
        
        for index, num in enumerate(nums):
            n = target - num
            if n in hash_map:
                return ([hash_map[n], index])
            elif n not in hash_map:
                hash_map[num] = index 
        return []
    
l = Solution4()
print(l.two_sum([3,2,4], 7))



class Solution5:
    def pal_num(self, x):
        if x < 0:
            return False
        
        reverse = 0
        
        while x > 0:
            reverse = (reverse * 10) + (x % 10)
            x = x // 10
            
        return True if (x == reverse or x == reverse // 10) else False
        
l = Solution5()
print(l.pal_num(121))


# Roman numbers

class Solution6:
    def roman_to_int(self, s):
        roman_map = {"I": 1, "V": 5, "X": 10, 
                     "L": 50, "C": 100, "D": 500, 
                     "M": 1000
                    }
        
        current = 0
        previous = 0
        total = 0
        
        for i in range(len(s)):
            current = roman_map[s[i]]
            if current > previous:
                total = total + current - 2 * previous
            else:
                total += current 
            previous = current
        return total 
    
l = Solution6()
print(l.roman_to_int("LVIII"))
        
        
# longest common prefix

class Solution7():
    def longest_common_prefix(self, s):
        
                
            