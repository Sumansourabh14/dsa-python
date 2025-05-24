# optimal solution
def largest_element(arr):
    max = arr[0]    
    for i in range(len(arr)):
        if (arr[i] > max):
            max = arr[i]
    return max

print(largest_element([1,2,4,7,7,5]))

# O(n) time complexity >>>>>>>> O(nlogn)