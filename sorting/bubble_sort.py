def bubble_sort(arr):
    for i in range(len(arr) - 1, 0, -1):
        # on the first iteration, if no swaps (means already sorted), break out of the loop and return arr
        is_swapped = False
        for j in range(i):
            if (arr[j] > arr[j + 1]):
                temp = arr[j + 1]
                arr[j + 1] = arr[j]
                arr[j] = temp
                is_swapped = True
        if is_swapped == False:
            break
    return arr

print(bubble_sort([13, 24, 46, 52, 20, 9]))
print(bubble_sort([13, 24, 46, 52, 90]))

# O(n)^2 - worst case
# O(n) - best case