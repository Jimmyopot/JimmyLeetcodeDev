# soln 1

def bubble_sort(num_list):
    n = len(num_list)
    
    for i in range(n-1):
        for j in range(n-i-1):
            if num_list[j] > num_list[j+1]:
                num_list[j], num_list[j+1] = num_list[j+1], num_list[j] # swap
    return num_list
                
print(bubble_sort([3, 10, 56, 1, 8, 18, 47, 12, 34]))



# soln 2

def sort(nums):
    
    for i in range(len(nums)-1,0,-1):  # end of list, back to beginning, then end again
        for j in range(i):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j] # swap
    return nums
                
print(sort([3, 10, 56, 1, 8, 18, 47, 12, 34]))



# soln 3

def bubble(list_a):
    indexing_length = len(list_a) - 1
    sorted = False
    
    while not sorted:
        sorted = True
        for i in range(0, indexing_length):
            if list_a[i] > list_a[i+1]:
                sorted = False
                list_a[i], list_a[i+1] = list_a[i+1], list_a[i]
    return list_a
                
print(bubble([3, 6, 0, 9, 4, 1, 6]))
