# https://leetcode.com/problems/contains-duplicate/

# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
def containsDuplicate(arr):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if (arr[i] == arr[j]):
                return True
    return False

print(containsDuplicate([1, 2, 3, 2, 2, 3, 3]))
print(containsDuplicate([1, 2, 3]))

def contains_duplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False

print(contains_duplicate([1, 2, 3, 2, 2, 3, 3]))
print(contains_duplicate([1, 2, 3]))
