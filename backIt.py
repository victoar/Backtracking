sol = []
numbers = []

def increasingOrder(a, b):
    if a < b:
        return True
    return False

def commonDigit(a, b):
    ok = 0
    while a > 0:
        x = b
        c1 = a % 10
        a = int(a / 10)
        while x > 0:
            c2 = x % 10
            if c1 == c2:
                ok = 1
            x = int(x / 10)
    if ok == 1:
        return True
    return False

def checkSubsequence(sol):
    ok = 1
    for i in range(1, len(sol)):
        if increasingOrder(sol[i - 1], sol[i]) == False or commonDigit(sol[i - 1], sol[i]) == False:
            ok = 0
    if ok == 1:
        return True
    return False

def transformSubsequenceIt(k):
    global sol, numbers
    list = []
    for i in range(1, k):
        if sol[i] == 1:
            list.append(numbers[i - 1])
    return list

def printSol(sol):
    length = len(sol)
    for i in range(0, length):
        print(sol[i], end = " ")
    print()

def valid(k):
    global sol
    num = 0
    for i in range(1, k):
        if sol[i] == 1:
            num += 1
    if num < 2:
        return False
    return True

def back(n):
    k = 1
    while k > 0:
        if k == n + 1:
            if valid(k) == True:
                list = transformSubsequenceIt(k)
                if checkSubsequence(list) == True:
                    printSol(list)
            k -= 1
        elif sol[k] < 1:
            sol[k] = sol[k] + 1
            k += 1
        elif sol[k] >= 1:
                sol[k] = -1
                k -= 1

def readn():

    global sol
    n = input('n = ')
    n = int(n)
    for i in range(0, n):
        number = input()
        number = int(number)
        numbers.append(number)
    sol = [-1] * (n + 1)
    back(n)


readn()