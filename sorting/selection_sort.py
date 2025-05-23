# move minimum to left after each iteration
def selection_sort(arr):
    for i in range(len(arr)):
        mini = i
        for j in range(i + 1, len(arr)):
            if (arr[j] < arr[mini]):
                mini = j
        temp = arr[mini]
        arr[mini] = arr[i]
        arr[i] = temp
    return arr

print(selection_sort([13, 46, 24, 52, 20, 9]))

