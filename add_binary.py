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
        a_decimal = 0
        b_decimal = 0
        
        a = a[::-1]  # this just means reverse list
        b = b[::-1]
        a = list(a)  # make a and b into a list
        b = list(b)
        i = 0
        
        while i < len(a):
            if a[i] == "1":
                a_decimal += 2**i
            i += 1
        while i < len(b):
            if b[i] == "1":
                b_decimal += 2**i
            i += 1
            
        return bin(a_decimal + b_decimal)[2:]
    
l = Solution()
print(l.addBinary("11", "1"))