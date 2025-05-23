# https://leetcode.com/submissions/detail/1640487059/

def smallestIndex(nums):
    for i in range(len(nums)):
        sum = 0
        while (nums[i] > 0):
            r = nums[i] % 10
            sum = sum + r
            nums[i] = nums[i] // 10
        if (sum == i):
            return i
    return -1

print(smallestIndex([1,3,2]))
print(smallestIndex([1,10,11]))
print(smallestIndex([1,2,3]))