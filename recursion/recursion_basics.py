def printName(name, n):
    if (n == 0):
        return
    print(name)
    printName(name, n - 1)

# printName("Rock", 2)

def printName1(name, n, i = 1):
    if (i > n):
        return
    print(name)
    printName1(name, n, i + 1)

# printName1("Martin", 3)

# print 1 to n times
def print1ToNTimes(n, i = 1):
    if (i > n):
        return
    print(i)
    print1ToNTimes(n, i + 1)

# print1ToNTimes(7)

# print n to 1 times
def printNTo1Times(n):
    if (n == 0):
        return
    print(n)
    printNTo1Times(n - 1)

# printNTo1Times(4)

# sum of first N numbers
# Parameterized method
def printSum(n, sum = 0, i = 1):
    if (i == n + 1):
        return sum
    sum += i
    i += 1
    return printSum(n, sum, i)

# print(printSum(4))

# sum of first N numbers
# Functional method
def printSumFuntionalWay(n):
    if (n == 0):
        return 0
    return n + printSumFuntionalWay(n - 1)

# print(printSumFuntionalWay(10)) 

# factorial of a number
def factorial(n):
    if (n == 0): 
        return 1
    return n * factorial(n - 1)

# print(factorial(4))

def factorialParam(n, i = 1, fact = 1):
    if (i == n + 1):
        return fact
    return factorialParam(n, i + 1, fact * i)

# print(factorialParam(4))

# reverse an array
def reverseArray(a):
    l = 0
    r = len(a) - 1
    for _ in range(len(a) // 2):
        a[l], a[r] = a[r], a[l]     # swap
        l += 1
        r -= 1
    return a

print(reverseArray([1,4,3,2]))

def reverseArrayRecursion(a):
    def helper(l, r):
        if l >= r:
            return
        a[l], a[r] = a[r], a[l]
        helper(l + 1, r - 1)
    helper(0, len(a) - 1)
    return a

print(reverseArrayRecursion([1,4,3,2]))

        