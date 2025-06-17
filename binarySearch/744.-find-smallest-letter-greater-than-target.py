# https://leetcode.com/problems/find-smallest-letter-greater-than-target
# Upper bound

def nextGreatestLetter(letters, target):
    """
    :type letters: List[str]
    :type target: str
    :rtype: str
    """
    n = len(letters)
    low = 0
    high = n - 1
    ans = letters[0]

    while (low <= high):
        mid = (low + high) // 2

        if (letters[mid] > target):
            ans = letters[mid]
            high = mid - 1
        else:
            low = mid + 1
    
    return ans