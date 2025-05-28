# 2 pointers
def palindrome(s):
    l = 0
    r = len(s) - 1
    while (l < r):
        if (s[l] != s[r]):
            return s, 'NOT a palindrome!'
        l += 1
        r -= 1
    return s, 'A palindrome!'

print(palindrome("faf"))
print(palindrome("fafag"))