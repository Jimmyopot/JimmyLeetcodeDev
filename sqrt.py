# soln 1

class Solution(object):
    def mySqrt(self, x):
        if x < 2:
            return x
        
        low = 0
        high = x
        
        # use BINARY SEARCH
        while low <= high:
            mid = (low + high) // 2  # this is FLOOR, e.g (5 // 2) = 2 and not 2.5
            if mid * mid <= x < (mid + 1) * (mid + 1):
                return mid
            elif x < mid * mid:
                high = mid
            else:
                low = mid
                
l = Solution()
print(l.mySqrt(8))
# time complexity = O(log n)



# soln 2*********************BEST SOLN**************************

class Solution2(object):
    def mySqrt2(self, x):
        left = 0
        right = x
        # again, use BINARY SEARCH [left......mid.....right]
        
        while left <= right:
            mid = (left + right) // 2  # floor returns whole number
            mid_squared = mid * mid
            
            if mid_squared <= x:
                left = mid + 1
            else:
                right = mid - 1
                
        return left - 1
        '''
        e.g, 15:
        -0 + 15 = 15 // 2 = 7
         7 * 7 = 49
         
        -0 + 7 = 7 // 2 = 3
         3 * 3 = 9
        
        '''
            
l = Solution2()
print(l.mySqrt2(10))



# soln 3

class Solution3(object):
    def mySqrt3(self, x):
        if x < 2:
            return x
        
        left = 1
        right = x // 2
        
        while left <= right:
            mid = left + (right + left) // 2
            if mid > x / mid:
                right = mid - 1
            else:
                left = mid + 1
        return left - 1
    
l = Solution3()
print(l.mySqrt3(12))
            