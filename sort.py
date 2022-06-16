# Andrew Yeh
# Sort algorithms
# CompSci 30
# Oct 7th
# This program is my own work - A.Y.


def bubbleSort(listSort):
    for i in range(len(listSort)):
        for sortNum in range(len(listSort) - 1 - i):
            if listSort[sortNum] < listSort[sortNum + 1]:
                listSort[sortNum + 1], listSort[sortNum] = listSort[sortNum], listSort[sortNum + 1]
        print(listSort)


def selectionSort(listSort):
    for i in range(len(listSort)):
        largestIndex = 0
        for j in range(len(listSort) - i):
            if listSort[j] > listSort[largestIndex]:
                largestIndex = j
        listSort.append(listSort[largestIndex])
        listSort.pop(largestIndex)
        print(listSort)


def insertionSort(listSort):
    for i in range(len(listSort)):
        n = 0
        while listSort[i] < listSort[n]:
            n += 1
        save = listSort[i]
        listSort.pop(i)
        listSort.insert(n, save)
        print(listSort)


again = "y"
while again == "y":
    sort = input('input "b" for bubble sort :: "s" for selection sort :: "i" for insertion sort ')
    primeList = [89, 2, 71, 37, 11, 59, 97, 83, 5, 47, 13, 67, 7, 19, 3, 17, 31, 43, 29, 41, 23, 53, 61, 73, 79]
    print(primeList)
    if sort == "b":
        bubbleSort(primeList)
    elif sort == "s":
        selectionSort(primeList)
    else:
        insertionSort(primeList)
    again = input("Again? (y or n) ")
