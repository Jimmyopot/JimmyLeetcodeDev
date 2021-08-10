'''
- Divide and conqure algorithm.
- Merge sort is RECURSIVE(method calls itself).
- Merge sort works:
  # Splitting the input list into two halves.
  # Repeating the process on those halves.
  # Finally merging the two sorted halves together.
'''

# soln 1

def mergeSort(myList):
    if len(myList) > 1:
        mid = len(myList) // 2
        left = myList[:mid]
        right = myList[mid:]
        
        # Recusively call on each half
        mergeSort(left)
        mergeSort(right)
        
        # 2 iterarors for traversing both halves
        i = 0
        j = 0
        
        k = 0  # Iterator for the main list
    
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                # The value from the left half has been used
                myList[k] = left[i]
                i += 1  # Move the iterator forward
                k += 1
            else:
                myList[k] = right[j]
                j += 1  # Move to next slot
                k +=1
                
        # For all remaining values
        while i < len(left):
            myList[k] = left[i]
            i += 1
            k += 1
        
        while  j < len(right):
            myList[k] = right[j]
            j += 1
            k += 1
            
    return myList
        
print(mergeSort([54,26,93,17,77,31,44,55,20]))

# Time complexity: O(n log n)





# soln 2 (TREEHOUSE FREE CODE CAMP)

"""
Sort a list in ascending order
Return a new sorted list

- 3 steps:
   # Divide: Find midpoint of the list and divide into sublists
   # Conquer: Recursively sort the sublists created in previous step
   # Combine: Merge the sorted sublists created in previous step
   
   Takes O(n log n) time
"""

def merge_sort(values):
    if len(values) <= 1:
        return values
    
    middle_index = len(values) // 2
    left_values = merge_sort(values[:middle_index])  # recursively call left half
    right_values = merge_sort(values[middle_index:])  # recursively call right half
    sorted_values = []
    
    left_index = 0  # left pointer
    right_index = 0  # right pointer
    
    while left_index < len(left_values) and right_index < len(right_values):
        if left_values[left_index] < right_values[right_index]:
            sorted_values.append(left_values[left_index])
            left_index += 1
        else:
            sorted_values.append(right_values[right_index])
            right_index += 1
            
    sorted_values += left_values[left_index:]
    sorted_values += right_values[right_index:]
    return sorted_values

sorted_numbers = merge_sort([47, 18, 45, 92, 45, 32, 12, 8, 67])
print(sorted_numbers)

# Time complexity: O(n log n)

