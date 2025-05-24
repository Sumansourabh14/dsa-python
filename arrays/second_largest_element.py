# Better solution
# O(2n) time complexity
def second_largest_element(arr):
    largest = arr[0]    
    for i in range(len(arr)):
        if (arr[i] > largest):
            largest = arr[i]

    second_largest = -1
    for i in range(len(arr)):
        if (arr[i] > second_largest and arr[i] != largest):
            second_largest = arr[i]

    return second_largest


print(second_largest_element([1,2,4,7,7,5]))


# Optimal solution
# O(n) time complexity
def second_largest_element_optimal(arr):
    largest = arr[0]
    second_largest = -1   
    for i in range(len(arr)):
        if (arr[i] > largest):
            second_largest = largest
            largest = arr[i]
        elif (arr[i] < largest and arr[i] > second_largest):
            second_largest = arr[i]
    return second_largest


print(second_largest_element_optimal([1,2,4,7,7,5]))