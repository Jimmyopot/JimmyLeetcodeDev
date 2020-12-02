# soln 1
arr1 = [1, 3, 5, 6]
target1 = 8

arr2 = [4, 7, 2, 6]
target2 = 12

def two_sum(arr, target):
    values = dict()
    
    for i, elem in enumerate(arr):
        comp = target - elem
        
        if comp in values:
            return [values[comp], i]
        values[elem] = i
        
    return []

list1 = two_sum(arr1, target1)  #[1, 2]
print(list1)   

list2 = two_sum(arr2, target2)   #[]
print(list2)


# soln 2
class Solution:
    def two_sum(self, nums, target):
        compliments = {} # this is a hash map
        results = []
        for index, num in enumerate(nums): # enumerate is used to get index and values in list in nums
            if compliments.get(num) is None:
                compliments[target - num] = index
            else:
                result = [compliments[num], index]
        return result
    
l = Solution()
print(l, two_sum([], 27))              # []
print(l, two_sum([2, 7, 11, 15], 9))   # [0, 1]
print(l, two_sum([2, 7, 11, 15], 26))  # [2, 3]


# soln 3 *************************USED THIS****************************
class Solution:
    def two_sum(self, nums, target):
        seen = {}
        
        for index, num in enumerate(nums):
            n = target - num
            if n in seen:
                return([seen[n], index])
            elif n not in seen:
                seen[num] = index
                
l = Solution()
print(l, two_sum([], 27))              # []
print(l, two_sum([2, 7, 11, 15], 9))   # [0, 1]
print(l, two_sum([2, 7, 11, 15], 26))
                
                
# soln 4 (i is at index 0 and j is at last index)
nums = [-2, 1, 2, 4, 7, 11]
target = 6

def two_sum(nums, target):
    i = 0
    j = len(nums) - 1
    
    while i <= j:
        if nums[i] + nums[j] == target:
            print(nums[i], nums[j])
            return True
        elif nums[i] + nums[j] < target:
            i += 1
        else:
            j -= 1
    return False

print(two_sum(nums, target)) # [2, 4]
# Time complexity = O(n)
# Space complexity = O(1)           



# soln 5 (brute force/ double forloop)
nums = [-2, 1, 2, 4, 7, 11]
target = 15

def bruteForcetwoSum(nums, target):
    for i in range(len(nums)-1):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return[i, j]
            
print(bruteForcetwoSum(nums, target))  #[3, 5]
# Time complexity = O(n^2)
# Space complexity = O(1)



# soln 6 (sorting)
nums3 = [14, 10, 3, 19, 7, 20, 34, 9, 15, 6]
target3 = 44

class Solution:
    def two_sum(self, nums, target):
        new_nums = sorted(zip(nums, range(len(nums))))
        # print(new_nums)
                          
        left = 0
        right = len(nums) - 1
        
        while left < right:
            current = new_nums[left][0] + new_nums[right][0]
            if current == target:
                return [new_nums[left][1], new_nums[right][1]]
            
            if current < target:
                left += 1
            else:
                right -= 1
                
l = Solution()
print(l, two_sum(nums3, target3))              
# print(l, two_sum([2, 7, 11, 15], 9))   
# print(l, two_sum([2, 7, 11, 15], 26))
                
