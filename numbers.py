# Andrew Yeh
# Numbers program
# CompSci 30
# Oct 21st
# This program is my own work - A.Y.

def bubbleSort(listSort):
    for i in range(len(listSort)):
        for sortNum in range(len(listSort) - 1 - i):
            if listSort[sortNum] > listSort[sortNum + 1]:
                listSort[sortNum + 1], listSort[sortNum] = listSort[sortNum], listSort[sortNum + 1]
    return listSort

numList = [51, 68, 15, 90, 78, 97, 14, 56, 81, 79, 26, 80, 48, 64, 37, 88, 94, 91, 6, 44, 49, 9, 34, 85, 25, 95, 67, 11, 47, 58, 65, 50, 61, 100, 36, 40, 63, 5, 89, 57, 45, 53, 30, 4, 69, 71, 82, 77, 59, 74, 75, 10, 27, 72, 86, 24, 31, 52, 3, 23, 41, 46, 32, 38, 21, 62, 55, 83, 43, 16, 98, 33, 12, 7, 60, 66, 54, 18, 92, 29, 35, 8, 20, 96, 1, 76, 17, 93, 73, 84]

numList = bubbleSort(numList)
print("Sorted list:")
print(numList)
for i in range(100):
    if i != 0:
        if i not in numList:
            for j in range(len(numList)):
                if numList[j] > i:
                    numList.insert(j, i)
                    break
print("Add missing numbers:")
print(numList)
print("Here is the list of primes:")
primeList = []
for i in numList:
    prime = True
    for j in range(2, i):
        if (i / j).is_integer():
            prime = False
            break
    if prime and i != 1:
        primeList.append(i)
print(primeList)
fibList = [1, 1]
while fibList[-1] + fibList[-2] <= 100:
    fibList.append(fibList[-1] + fibList[-2])
print("Here is the fibonacci sequence up to 100:")
print(fibList)
