# soln 1 **********************************BEST SOLN *********************************

class Solution(object):
    def searchInsert(self, nums, target):
        '''
        - use binary search.
        - use left and right pointer to get mid...
        - (left + right )/ 2 to get mid.
        - compare mid with the target.
        
        - [2, 5, 6, 8, 9, 12, 14, 17]
           l (0)                   r len(nums) - 1
        '''
        r = len(nums) - 1
        l = 0
        
        while l <= r:
            mid = (l + r) // 2  # // means floor (Round numbers down to the nearest integer)
            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                r = mid - 1
            else:
                l = mid + 1
        return l
    
s = Solution()
print(s.searchInsert([1,3,5,6], 2))
# time complexity = O(logn) cutting list to half
# space complexity = O(1)



# soln 2

class Solution2(object):
    def searchInsert2(self, nums, target):
        
        if target > nums[len(nums) - 1]:
            return len(nums)
        
        for i in range(len(nums)):
            if nums[i] >= target:
                return i
            
s = Solution2()
print(s.searchInsert2([1,3,5,6], 2))
                