# https://leetcode.com/problems/find-words-containing-character/description/

def findWordsContaining(words, x):
    newSet = set()
    for i in range(len(words)):
        for j in range(len(words[i])):
            if (words[i][j] == x):
                newSet.add(i)

    return list(newSet)

print(findWordsContaining(["leet","code"], "e"))
print(findWordsContaining(["abc","bcd","aaaa","cbc"], "z"))