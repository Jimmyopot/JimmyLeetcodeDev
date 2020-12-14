# soln 1

class Solution(object):
    def countAndSay(self, n):
        seq = "1"
        
        for i in range(n-1):
            seq = self.getNext(seq)
        return seq
    
    def getNext(self, seq):
        i, next_seq = 0, ""
        
        while i < len(seq):
            count = 1
            while i < len(seq) - 1 and seq[i] == seq[i+1]:
                count += 1
                i += 1
            next_seq += str(count) + seq[i]
            i += 1
        return next_seq
    
l = Solution()
print(l.countAndSay(1234))



# soln 2

class Solution2(object):
    def countAndSay2(self, n):
        if n == 1:
            return "1"
        else:
            prev_sequence = self.countAndSay(n-1)
            
            result_sequence = ""
            counter = {}
            
            for i in range(0, len(prev_sequence)):
                digit = prev_sequence[i]
                
                if digit not in counter:
                    for key, value in counter.items():
                        result_sequence += str(value) + key 
                    counter = {}
                    counter[digit] = 1
                else:
                    counter[digit] += 1
            
            for key, value in counter.items():
                result_sequence += str(value) + key
                
            return result_sequence
        
l = Solution2()
print(l.countAndSay2(1234))



# soln 3

class Solution3(object):
    def countAndSay3(self, n):
        if n == 1:
            return "1"
        elif n == 2:
            return "11"
        
        # Find n'th term by generating all terms from 3 to n-1. Every term is generated using previous term 
        
        # Initialize previous term
        s = "11"
        
        for i in range(3, n+1):
            s += "$"
            l = len(s)
            # In the for loop, previous character is processed in current iteration. That is why a dummy character is added to make sure that loop runs one extra iteration. 
            
            count = 1  # Initialize count of matching chars
            temp = ""  # Initialize i'th term in series 
            
            # Process previous term to find the next term 
            for j in range(1, l):
                
                # If current character does't match
                if s[j] != s[j - 1]:  
                    temp += str(count + 0)  # Append count of str[j-1] to temp
                    temp += s[j - 1]   # Append str[j-1] 
                    count = 1  # Reset count 
                    
                else:  # If matches, then increment count of matching characters 
                    count += 1
                    
            s = temp  # Update str
            
            return s;
    
    
    
# soln 4 ********************************BEST SOLUTION**********************************

class Solution4(object):
    def countAndSay4(self, n):
        s = "1"
        if n == 1:
            return s
        for i in range(2,n+1):
            j = 0
            temp = ""
            curr = ""
            count = 0
            while j<len(s):
                #print(curr,count)
                if curr =="":
                    #print(curr)
                    curr=s[j]
                    count=1
                    j+=1
                elif curr == s[j]:
                    #print(curr)
                    count+=1
                    j+=1
                else:
                    #print(count,curr)
                    temp+= str(count) + curr
                    curr=""
                    count = 0
                    #print(temp)
            temp+=str(count) + curr
            s=temp
        return s
    
ob1 = Solution4()
print(ob1.countAndSay4(6))