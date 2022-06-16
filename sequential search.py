# Andrew Yeh
# Sequential Sort
# CompSci 30
# Oct 31st
# This program is my own work - A.Y.

playerList = [15, 22, 75, 5, 29, 37, 23, 18, 44, 2, 20, 19, 97, 71, 93, 25, 13, 4, 10, 14, 41, 8, 56]

target = int(input("Please enter a number that you would like to search: "))

found = False
for i in range(len(playerList)):
    print(f"Checking if {playerList[i]} matches with the target of {target}.")
    if playerList[i] == target:
        print(f"Your target was found at index {i}.")
        found = True
        break
    print("It is not a match.")
if not found:
    print("Your target was not in the list")
