def drawboard(board):
    # This function prints out the board that it was passed.
    print('\n     |     |')
    print('  ' + board[0] + '  |  ' + board[1] + '  |  ' + board[2])
    print('     |     |')
    print('------------------')
    print('     |     |')
    print('  ' + board[3] + '  |  ' + board[4] + '  |  ' + board[5])
    print('     |     |')
    print('------------------')
    print('     |     |')
    print('  ' + board[6] + '  |  ' + board[7] + '  |  ' + board[8])
    print('     |     |')


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


def playerInput(board: list, player: str):
    inputPos = int(input(f"\nPlayer {player}, please choose your spot: "))
    while board[inputPos - 1] == 'y' or board[inputPos - 1] == 'x':
        inputPos = int(input("\nThat space is already taken, try again: "))
    board[inputPos - 1] = player
    drawboard(board)
    if checkWin(board, player):
        print(f"\nCongrats! Player {player} wins!")
        return False
    elif board.count('x') + board.count('o') >= 9:
        print("You tied")
        return False
    return True


def main():
    print("Welcome to Tic Tac Toe! Play with your friends!")  # instructions
    print("This is the number corresponding to each spot on the board: ")
    print()
    # shows the places
    drawboard(['1', '2', '3', '4', '5', '6', '7', '8', '9'])
    print()
    print("Ready to play? Lets start!")

    again = "yes"  # play again
    while again == "yes":  # play again
        playing = True
        player = 'x'
        board = [' '] * 10
        while playing:
            playing = playerInput(board, player)
            if player == 'o':
                player = 'x'
            elif player == 'x':
                player = 'o'
        again = input("\nPlay another round? (yes or no) ").lower()  # play again
        again = again.lower()


if __name__ == "__main__":
    main()
