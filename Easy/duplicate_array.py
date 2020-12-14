# soln 1

class Solution(object):
    def removeDuplicates(self, nums):
        n = len(nums)
        if n <= 1:
            return n
        i = j = 1
        
        while i < n:
            if nums[i] != nums[i-1]:
                nums[j] = nums[i]
                j += 1
            i += 1
        return j
    
l = Solution()
print(l.removeDuplicates([0,0,1,1,2,2,3,3]))



# soln 2

class Solution2(object):
    def removeDuplicates2(self, nums):
        # use 2 pointers
        i = 0
        j = 0
        
        for j in range(len(nums)):
            if nums[j] != nums[i]:
                i += 1  # this means increment to next index
                nums[i] = nums[j]
        return i + 1
    
l = Solution2()
print(l.removeDuplicates2([0,0,1,1,2,2]))
# time complexity O(n) [we only go through the list once]
# space complexity O(1)



# soln 3

class Solution3(object):
    def removeDuplicates3(self, nums):
        i = 0
        
        while i < len(nums):
            if nums[i] in nums[i+1:]:  # this is slicing to the end *[1:]
                nums.remove(nums[1])
            else:
                i += 1
        return i
    
l = Solution3()
print(l.removeDuplicates3([0,0,1,1,2,2,4,5,5,7,8,8]))