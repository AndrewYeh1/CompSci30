theBoard = [' '] * 10

print("Welcome to Tic Tac Toe! Play with your friends!")  # instructions
print("This is the number corresponding to each spot on the board: ")
print('')
# shows the places
print('     |     |')
print('  1  |  2  |  3')
print('     |     |')
print('------------------')
print('     |     |')
print('  4  |  5  |  6')
print('     |     |')
print('------------------')
print('     |     |')
print('  7  |  8  |  9')
print('     |     |')

print("\nReady to play? Lets start!")

again = "yes"  # play again
while again == "yes":  # play again
    theBoard = [' '] * 10


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


    drawboard(theBoard)


    def person():  # gets player 1 input, checks to see if it is valid and if they won
        pone = int(input("\nFirst player, please choose your spot: "))
        while theBoard[pone - 1] == 'o' or theBoard[pone - 1] == 'x':
            pone = int(input("\nThat space is already taken, try again: "))
        theBoard[pone - 1] = 'x'
        drawboard(theBoard)
        # conditions to win
        if (theBoard[0:3] == ['x', 'x', 'x']) or (theBoard[3:6] == ['x', 'x', 'x']) \
                or (theBoard[6:9] == ['x', 'x', 'x']) \
                or (theBoard[0] == 'x' and theBoard[3] == 'x' and theBoard[6] == 'x') \
                or (theBoard[1] == 'x' and theBoard[4] == 'x' and theBoard[7] == 'x') \
                or (theBoard[2] == 'x' and theBoard[5] == 'x' and theBoard[8] == 'x') \
                or (theBoard[0] == 'x' and theBoard[4] == 'x' and theBoard[8] == 'x') \
                or (theBoard[2] == 'x' and theBoard[4] == 'x' and theBoard[6] == 'x'):
            print("\nCongrats! Player 1 wins!")
        return


    def opponent():  # function to get player 2s input, check it, and check it they win
        two = int(input("\nSecond player, please choose your spot: "))
        while theBoard[two - 1] == 'y' or theBoard[two - 1] == 'x':
            two = int(input("\nThat space is already taken, try again: "))
        theBoard[two - 1] = 'o'
        drawboard(theBoard)
        # conditions to win
        if (theBoard[0:3] == ['o', 'o', 'o']) or (theBoard[3:6] == ['o', 'o', 'o']) \
                or (theBoard[6:9] == ['o', 'o', 'o']) \
                or (theBoard[0] == 'o' and theBoard[3] == 'o' and theBoard[6] == 'o') \
                or (theBoard[1] == 'o' and theBoard[4] == 'o' and theBoard[7] == 'o') \
                or (theBoard[2] == 'o' and theBoard[5] == 'o' and theBoard[8] == 'o') \
                or (theBoard[0] == 'o' and theBoard[4] == 'o' and theBoard[8] == 'o') \
                or (theBoard[2] == 'o' and theBoard[4] == 'o' and theBoard[6] == 'o'):
            print("\nCongrats! Player 2 wins!")
        return

    places = 0
    while places < 9:
        # conditions to either loop the calls for functions or end the game
        while (theBoard[0:3] != ['x', 'x', 'x']) and (theBoard[3:6] != ['x', 'x', 'x']) \
                and (theBoard[6:9] != ['x', 'x', 'x']) \
                and (theBoard[0] != 'x' or theBoard[3] != 'x' or theBoard[6] != 'x') \
                and (theBoard[1] != 'x' or theBoard[4] != 'x' or theBoard[7] != 'x') \
                and (theBoard[2] != 'x' or theBoard[5] != 'x' or theBoard[8] != 'x') \
                and (theBoard[0] != 'x' or theBoard[4] != 'x' or theBoard[8] != 'x') \
                and (theBoard[2] != 'x' or theBoard[4] != 'x' or theBoard[6] != 'x') \
                and (theBoard[0:3] != ['o', 'o', 'o']) and (theBoard[3:6] != ['o', 'o', 'o']) \
                and (theBoard[6:9] != ['o', 'o', 'o']) \
                and (theBoard[0] != 'o' or theBoard[3] != 'o' or theBoard[6] != 'o') \
                and (theBoard[1] != 'o' or theBoard[4] != 'o' or theBoard[7] != 'o') \
                and (theBoard[2] != 'o' or theBoard[5] != 'o' or theBoard[8] != 'o') \
                and (theBoard[0] != 'o' or theBoard[4] != 'o' or theBoard[8] != 'o') \
                and (theBoard[2] != 'o' or theBoard[4] != 'o' or theBoard[6] != 'o'):
            person()
            places = theBoard.count('x') + theBoard.count('o')
            print(places)
            if places == 9:
                print("You tied!")
                break
            if (theBoard[0:3] != ['x', 'x', 'x']) and (theBoard[3:6] != ['x', 'x', 'x']) and (
                    theBoard[6:9] != ['x', 'x', 'x']) \
                    and (theBoard[0] != 'x' or theBoard[3] != 'x' or theBoard[6] != 'x') \
                    and (theBoard[1] != 'x' or theBoard[4] != 'x' or theBoard[7] != 'x') \
                    and (theBoard[2] != 'x' or theBoard[5] != 'x' or theBoard[8] != 'x') \
                    and (theBoard[0] != 'x' or theBoard[4] != 'x' or theBoard[8] != 'x') \
                    and (theBoard[2] != 'x' or theBoard[4] != 'x' or theBoard[6] != 'x'):
                opponent()
                places = theBoard.count('x') + theBoard.count('o')
                print(places)
                if places == 10:
                    print("You tied!")
                    break
    again = input("\nPlay another round? (yes or no) ").lower()  # play again
    again = again.lower()
print("\nThanks for playing!")
