# https://leetcode.com/problems/largest-odd-number-in-string/description/

def largestOddNumber(num):
    for i in range(len(num) - 1, -1, -1):
        if int(num[i]) % 2 != 0:
            return num[:i+1]
    return ""

print(largestOddNumber("52"))
print(largestOddNumber("4206"))
print(largestOddNumber("35427"))
print(largestOddNumber("35428"))