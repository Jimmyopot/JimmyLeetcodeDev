"""
- Divide and conquer algorithm.
- It has a PIVOT. Breaks the list into 2
    > Less than pivot.
    > Greater than pivot.
- Sort the 2 lists by RECURSION!
"""

def quicksort(values):
    if len(values) <= 1:
        return values
    
    less_than_pivot = []
    greater_than_pivot = []
    pivot = values[0]
    
    for value in values[1:]:
        if value <= pivot:
            less_than_pivot.append(value)
        else:
            greater_than_pivot.append(value)
            
    return quicksort(less_than_pivot) + [pivot] + quicksort(greater_than_pivot)
    
sorted_numbers = quicksort([56,12,76,34,8,16,109,49])
print(sorted_numbers)
    
    