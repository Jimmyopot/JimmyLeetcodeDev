
# class Solution:
#     def two_sum(self, nums, target):
#         compliment = {}
#         for i, num in enumerate(nums):
#             n = target - num
#             if n in compliment:
#                 return ([compliment[n], i])
#             elif n not in compliment:
#                 compliment[num] = i 
#         return []

# l = Solution()       
# print(l, two_sum([2,7,11,15], 9))

# class Solution:
#     def two_sum(self, nums, target):
#         hash_map = {}  # this is a hash map
        
#         for index, num in enumerate(nums):
#             n = target - num
#             if n in hash_map:
#                 return([hash_map[n], index])
#             elif n not in hash_map:
#                 seen[num] = index
                
# l = Solution()
# print(l, two_sum([], 27))              # []
# print(l, two_sum([2, 7, 11, 15], 9))   # [0, 1]
# print(l, two_sum([2, 7, 11, 15], 26))



arr1 = [1, 3, 5, 6]
target1 = 8

arr2 = [4, 7, 2, 6]
target2 = 12

def two_sum(arr, target):
    values = dict()
    
    for index, num in enumerate(arr):
        n = target - num
        if n in values:
            return (values[n], index)
        elif n not in values:
            values[num] = index
    return[]

list1 = two_sum(arr1, target1)  #[1, 2]
print(list1)   

list2 = two_sum(arr2, target2)   #[]
print(list2)


class Solution:
    def two_sum(self, nums, target):
        hash_map = {}  # this is a hash map
        
        for i, num in enumerate(nums):
            n = target - num 
            if n in hash_map:
                return ([hash_map[n], i])
            elif n not in hash_map:
                hash_map[num] = i
                
        return []
    
s = Solution()
print(s, two_sum([3,2,4], 6))