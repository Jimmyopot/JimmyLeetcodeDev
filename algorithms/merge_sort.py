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