def moveZerosToEnd(nums):
    j = -1
    for n in nums:
        if (n == 0):
            j = n
            break
    
    print(j)

    if (j == -1): return nums

    for i in range(len(nums)):
        if (nums[i] != 0):
            nums[i], nums[j] = nums[j], nums[i]
            j += 1
    
    return nums

print(moveZerosToEnd([0, 1, 0, 3, 12]))
print(moveZerosToEnd([1, 0, 1, 0, 3, 12]))