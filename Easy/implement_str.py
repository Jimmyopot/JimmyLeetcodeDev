# soln 1 ****************************BEST SOLN*****************************

class Solution(object):
    def strStr(self, haystack, needle):
        if not needle:
            return 0
        
        for i in range(len(haystack)):
            if haystack[i: i+len(needle)] == needle:
                return i
        return -1
    
l = Solution()
print(l.strStr("hello", "ll"))



# soln 2

class Solution2(object):
    def strStr2(self, haystack, needle):
        if len(needle) == 0:
            return 0
        
        for i in range(len(haystack) - len(needle) + 1):  # stop checking after finding the needle
            if haystack[i: i+len(needle)] == needle:
                return i
        return -1
    
l = Solution2()
print(l.strStr2("commute", "e"))