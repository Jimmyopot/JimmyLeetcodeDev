'''
- SELECTION SORT is a comparison sorting algorithm that is used to sort a random list of items in ascending order
- Check out the low value from left to right, then swap.
- Keep track of the low value.
- Better than bubble sort bcs there is only 1 swap per iteration. 
'''

# soln 1

def selection_sort(A):
    n = len(A)-1
    
    for i in range(0, n):
        # Find the minimum element in remaining unsorted array 
        low_value = i  # assume 1st element is the lowest
        
        for j in range(i+1, n):
            if A[low_value] > A[j]:
                low_value = j
               
        # Swap the found minimum element with the first element
        A[i], A[low_value] = A[low_value], A[i]
        
    return A

print(selection_sort([4, 7, 1, 2, 9, 5, 10, 8, 2, 5]))

# Time complexity: O(n^2)
# Space complexity: O(1)

