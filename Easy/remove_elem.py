# soln 1 ****************************BEST SOLUTION************************

class Solution(object):
    def removeElement(self, nums, val):
        k = 0  # first element(index) of array [nums]
        
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k
            
l = Solution()
print(l.removeElement([3,2,2,3,1,3,4,3], 3))



# soln 2

class Solution2(object):
    def removeElement2(self, nums, val):
        i = 0
        
        while i < len(nums):
            if nums[i] == val:
                nums.pop(i)
            else:
                i += 1
            
l = Solution2()
print(l.removeElement2([3,2,2,3,], 2))