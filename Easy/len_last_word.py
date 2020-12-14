# soln 1

class Solution(object):
    def lengthOfLastWord(self, s):
        s = s.split(' ')  # this splits words in a list ["Hello", "world"]
        
        if not s:
            return 0
        else:
            return len(s[-1])  # this will return last word in the list
    
l = Solution()
print(l.lengthOfLastWord(["Hello World Jim"]))



# soln 2

class Solution2(object):
    def lengthOfLastWord2(self, s):
        # len_s = "Hello world "
        len_s = len(s)
        len_word = 0
        
        # len(len_s) = 12
        
        while len_s > 0:
            len_s -= 1
            # len(len_s) = 11  (12-1=11)
            if s(len_s) != " ":
                len_word += 1
            elif len_word > 0:
                return len_word
            
        return len_word
    
l = Solution2()
print(l.lengthOfLastWord2(["Hello World Jim "]))



# soln 3

class Solution3(object):
    def lengthOfLastWord3(self, s):
        count = 0
        local_count = 0
        
        for i in range(len(s)):
            if s[i] == ' ':
                local_count = 0
            else:
                local_count += 1
                count = local_count
                
        return count
    
l = Solution3()
print(l.lengthOfLastWord3(["Hello World"]))
        