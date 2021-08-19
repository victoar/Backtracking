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

def printSol(sol):
    length = len(sol)
    for i in range(0, length):
        print(sol[i], end = " ")
    print()

solution = []
numbers = []

def backRecursive(index):

    global solution, numbers

    if checkSubsequence(solution) == True and len(solution) >= 2:
        printSol(solution)

    for i in range(index, len(numbers)):
        solution.append(numbers[i])
        backRecursive(i + 1)
        solution.pop()

    return

def readNumbers():

    global numbers
    n = input('n = ')
    n = int(n)
    for i in range(0, n):
        number = input()
        number = int(number)
        numbers.append(number)

    print('Recursive: \n')
    backRecursive(0)

readNumbers()
