# Andrew Yeh
# Binary Sort
# CompSci 30
# Oct 31st
# This program is my own work - A.Y.

playerList = [15, 22, 75, 5, 29, 37, 23, 18, 44, 2, 20, 19, 97, 71, 93, 25, 13, 4, 10, 14, 41, 8, 56]


def insertionSort(listSort):
    for i in range(len(listSort)):
        n = 0
        while listSort[i] < listSort[n]:
            n += 1
        save = listSort[i]
        listSort.pop(i)
        listSort.insert(n, save)
    return listSort
playerList = insertionSort(playerList)


target = int(input("Please enter a number that you would like to search: "))
found = False

print("Here is the list in order:")
print(playerList)


def binarySearch(listSearch, index):
    if listSearch[len(listSearch) // 2] < target:
        print(listSearch[:len(listSearch) // 2])
        result = binarySearch(listSearch[:len(listSearch) // 2], index)
    elif listSearch[len(listSearch) // 2] > target:
        print(listSearch[len(listSearch) // 2:])
        result = binarySearch(listSearch[len(listSearch) // 2:], index + len(listSearch) // 2)
    else:
        return len(listSearch) // 2 + index
    return result
print(f"Your target is at index {binarySearch(playerList, 0)}.")


