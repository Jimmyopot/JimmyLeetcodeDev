
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

class Solution:
    def two_sum1(self, nums, target):
        hash_map = {}  # this is a hash map
        
        for index, num in enumerate(nums):
            n = target - num
            if n in hash_map:
                return([hash_map[n], index])
            elif n not in hash_map:
                hash_map[num] = index
        return []
                
l = Solution()
print(l.two_sum1([], 27))              # []
print(l.two_sum1([2, 7, 11, 15], 9))   # [0, 1]
print(l.two_sum1([2, 7, 11, 15], 26))



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


# class Solution:
#     def two_sum(self, nums, target):
#         hash_map = {}  # this is a hash map
        
#         for i, num in enumerate(nums):
#             n = target - num 
#             if n in hash_map:
#                 return ([hash_map[n], i])
#             elif n not in hash_map:
#                 hash_map[num] = i
                
#         return []
    
# s = Solution()
# print(s, two_sum([3,2,4], 6))


class SolutionIndex:
    def twoSum(self, nums, target):
        my_dict = {}
        
        for index, num in enumerate(nums):
            n = target - num
            if n in my_dict:
                return ([my_dict[n], index])
            elif n not in my_dict:
                my_dict[num] = index
        return []
    
s = SolutionIndex()
print(s.twoSum([3,2,4], 6))


def my_function(x):
      return x[::-1]

mytxt = my_function("I wonder how this text looks like backwards")

print(mytxt)


class Soln:
    def two_sum(self, nums, target):
        hash_tbl = {}
        for i, num in enumerate(nums):
            n = target - num
            if n in hash_tbl:
                return (hash_tbl[n], i)
            elif n not in hash_tbl:
                hash_tbl[num] = i
        return []
    
l = Soln()
print(l.two_sum([3,6,7], 10))
<<<<<<< HEAD



def linear_search(list, target):
    for i in range(0, len(list)):
        if list[i] == target:
            return i
    return None

print(linear_search([1,2,3,4,5], 4))



def binary_search(list, target):
    first = 0
    last = len(list) -1
    
    while first < last:
        midpoint = first + last // 2
        if list[midpoint] == target:
            return midpoint
        elif list[midpoint] < target:
            first = midpoint + 1
        else:
            last = midpoint - 1 
    return None

print(binary_search([1,2,3,5,7,8], 6))
=======
>>>>>>> 586cb7c28738ccaef79f70aa4c7ea7b3192beeb0
