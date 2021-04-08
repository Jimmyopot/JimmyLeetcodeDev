
def linear_search(list, target):
    for i in range(0, len(list)):
        if list[i] == target:
            return i    
    return None

def verify(index):
    if index is not None:
        print("Target found at index: ", index)
    else:
        print("Target not found in list")
        
numbers = [3,5,2,1,6,7,8]

result = linear_search(numbers, 6)
verify(result)

print(linear_search([2,4,6,7], 4))
print(linear_search([2,4,6,7], 10))

# Runs in linear time, O(n)