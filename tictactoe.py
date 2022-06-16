# returns true if they won, returns false if they did not win yet
# player is either 'x' or 'o'
def checkWin(theBoard: list, player: str):
    # creates a list of all the possible combinations for winning
    winConditions = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    # iterates through all the combinations
    for i in winConditions:
        # checks if each combination is met
        if theBoard[i[0]] == player and theBoard[i[1]] == player and theBoard[i[2]] == player:
            # returns true if any of them are met
            return True
    # returns false if every combination is checked and there is none that are met
    return False

theBoardButOuterScope = ['x', 'o', 'o', 'o', 'x', 'o', 'o', 'o', 'o']
print((theBoardButOuterScope.count('x') + theBoardButOuterScope.count('o')) == 9)
print(checkWin(theBoardButOuterScope, 'x'))
