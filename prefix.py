#  soln 1

class Solution(object):
    def longestCommonPrefix(self, strs):
        if len(strs) == 0:
            return ""
        
        if len(strs) == 1:
            return (strs[0])
        
        prefix = strs[0]
        prefixlen = len(prefix)  # minimum length is 1st string in array
        
        for i in strs[1:]:  # starting from the 2nd prefix to the end...  
            while prefix != i[0:prefixlen]:
                prefix = prefix[0:(prefixlen-1)]
                prefixlen -= 1
                
                if prefixlen == 0:
                    return ""
                
        return prefix
    
l = Solution()
print(l.longestCommonPrefix(["flower","flow","flight"]))
        
        
        
# soln 2

class Solution1(object):
    def longestCommonPrefix1(self, strs):
        if len(strs) == 0:
            return ""
        elif len(strs) == 1:
            return strs[0]
        else:
            len_prefix = 0
            shortest_str = min(strs, key=len)
            '''
            - pick one of the strings in array and loop over characters.
            - pick shortest string to start with(shortest_str)...
            - a set only returns unique values.
            '''
            for i in range(len(shortest_str)):
                if len(set(word[i] for word in strs)) == 1:
                    len_prefix += 1
                else:
                    break
                
        if len_prefix == 0:
            return ""
        else:
            return shortest_str[:len_prefix]
        
l = Solution1()
print(l.longestCommonPrefix1(["common","compare","commit"]))



# soln 3

class Solution2(object):
    def longestCommonPrefix2(self, strs):
        if not strs:
            return ""
        
        minlen = len(strs[0])  # variable for 1st string in array
        
        for i in range(len(strs)):  # loop thro entire array
            minlen = min(len(strs[i]), minlen)
            
        lcp = ""  # variable that holds all common prefixes
        i = 0
        
        while i < minlen:
            char = strs[0][i]  # [0] represents 1st string, [i] represents 1st index in each string...
            for j in range(1, len(strs)):
                if strs[j][i] != char:
                    return lcp 
            lcp += char
            i += 1
        return lcp
    
l = Solution2()
print(l.longestCommonPrefix2(["common","compare","commit"]))