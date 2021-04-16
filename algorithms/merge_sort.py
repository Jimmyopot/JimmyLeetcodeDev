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

def merge_sort(list):
    if len(list) <= 1:
        return list
    
    left_half, right_half = split(list)
    left = merge_sort(left_half)  # recursion
    right = merge_sort(right_half)  # recursion
    
    return merge(left, right)

def split(list):
    """
    Divide the unsorted list at midpoint into sublists
    Returns 2 sublists - left and right
    Takes overall O(log n) time
    """
    
    mid = len(list) // 2  # floor division
    left = list[:mid]
    right = list[mid:]
    
    return left, right

def merge(left, right):
    """
    Merges 2 lists (arrays), sorting them in the process
    Returns a new merged list
    Takes O(n) time
    """
    
    l = []
    i = 0  # keeps track of the index values in left list
    j = 0  # keeps track of the index values in right list
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            l.append(left[i])
            i += 1
        elif left[i] > right[j]:
            l.append(right[j])
            j += 1
            
    while i < len(left):
        l.append(left[i])
        i += 1
        
    while j < len(right):
        l.append(right[j])
        j += 1
        
    return l

def verify_sorted(list):
    n = len(list)
    
    if n == 0 or n == 1:
        return True
    
    return list[0] < list[1] and verify_sorted(list[1:])
        
a_list = [47, 18, 45, 92, 45, 32, 12, 8, 67]
l = merge_sort(a_list)
# print(l)
print(verify_sorted(a_list))
print(verify_sorted(l))