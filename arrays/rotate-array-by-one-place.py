def rotate_array_by_one_place_left(a):
    temp = a[0]
    for i in range(1, len(a)):
        a[i - 1] = a[i]
    a[len(a) - 1] = temp
    return a

print(rotate_array_by_one_place_left([1,2,3,4,5]))