# soln 1  [KADANE'S ALGORITHM]************BEST SOLN************

class Solution(object):
    def maxSubArray(self, nums):
        '''
          0 1  2 3  4 5 6  7 8   ->(index)
        [-2,1,-3,4,-1,2,1,-5,4]  ->[array]
         -2 1 -2 4  3 5 6  1 5
         
         max(-2+1 or 1) = 1       max(3+2 or 2) = 5
         max(1+-3 or -3) = -2     max(5+1 or 1) = 6
         max(-2+4 or 4) = 4       max(6+-5 or -5) = 1
         max(4+-1 or -1) = 3      max(1+4 or 4) = 5
         
         therefore, max value = 6 
        '''
        total_sum = max_sum = nums[0]  # index of 1st elem in array
        
        for i in nums[1:]:
            total_sum = max(i, total_sum + i)
            max_sum = max(max_sum, total_sum)
            
        return max_sum
    
l = Solution()
print(l.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))



# soln 2

class Solution2(object):
    def maxSubArray2(self, nums):
        maxSub = nums[0]
        currSum = 0
        
        for n in nums:
            if currSum < 0:
                currSum = 0
            currSum += n
            maxSub = max(maxSub, currSum)
            
        return maxSub
       
l = Solution2()
print(l.maxSubArray2([-2,1,-3,4,-1,2,1,-5,4]))