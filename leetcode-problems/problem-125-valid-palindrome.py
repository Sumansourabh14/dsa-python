# https://leetcode.com/problems/valid-palindrome/

def isPalindrome(s):
    s1 = s.lower()

    s2 = ""
    for i in range(len(s1)):
        if s1[i].isalnum():
            s2 += s1[i]

    s3 = ""
    for i in range(len(s2) - 1, -1, -1):
        s3 += s2[i]

    if (s2 == s3):
        return True
    
    return False

print(isPalindrome("A man, a plan, a canal: Panama"))
print(isPalindrome("race a car"))
print(isPalindrome(" "))
print(isPalindrome("0P"))
    