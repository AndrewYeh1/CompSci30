# Ryan Fang
# Exercise 3 - Tic Tac Toe
# Computer Science 20
# May 14, 2021

# I took some inspiration from this website:
# https://medium.com/byte-tales/the-classic-tic-tac-toe-game-in-python-3-1427c68b8874
# I have rewritten and made modifications to the code (e.g. error checks, etc.)
# to make it more user friendly.

def print_board(board):
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[1] + '|' + board[2] + '|' + board[3])


play_again = "yes"

while (play_again == "yes"):

    # Initialize board

    board = {7: " ", 8: " ", 9: " ",
             4: " ", 5: " ", 6: " ",
             1: " ", 2: " ", 3: " "}

    board_keys = []

    for key in board:
        board_keys.append(key)

    turn = "X"  # X will start
    count = 0

    print_board(board)

    while (count < 9):

        # User interface

        move = input(turn + ", what place would you like to move too? ")

        while (not move.isdigit() or int(move) < 1 or int(move) > 9):
            move = input("Wrong input. Please enter a place: ")

        move = int(move)

        if (board[move] == " "):
            board[move] = turn
            count = count + 1

        else:
            print("That place is already filled. Choose another place.")
            continue

        # Check if a player won after 5 moves

        if (count >= 5):
            if (board[1] == board[4] == board[7] != " "):  # Down left side
                print_board(board)
                print("Game over! " + turn + " won.")
                break

            elif (board[2] == board[5] == board[8] != " "):  # Down middle
                print_board(board)
                print("Game over! " + turn + " won.")
                break

            elif (board[3] == board[6] == board[9] != " "):  # Down right side
                print_board(board)
                print("Game over! " + turn + " won.")
                break

            elif (board[7] == board[8] == board[9] != " "):  # Across top
                print_board(board)
                print("Game over! " + turn + " won.")
                break

            elif (board[4] == board[5] == board[6] != " "):  # Across middle
                print_board(board)
                print("Game over! " + turn + " won.")
                break

            elif (board[1] == board[2] == board[3] != " "):  # Across bottom
                print_board(board)
                print("Game over! " + turn + " won.")
                break

            elif (board[7] == board[5] == board[3] != " "):  # Diagonal starting in top left
                print_board(board)
                print("Game over! " + turn + " won.")
                break

            elif (board[1] == board[5] == board[9] != " "):  # Diagonal starting in bottom left
                print_board(board)
                print("Game over! " + turn + " won.")
                break

        # Tie if neither X or O wins after 9 moves

        if count == 9:
            print("Game over. It's a tie!")

            # Change player every move

        if (turn == "X"):
            turn = "O"

        else:
            turn = "X"

        print_board(board)

    # Play again

    play_again = input("Do want to play again (yes/no)? ").lower()

    while (play_again != "yes" and play_again.lower() != "no"):
        play_again = input("Wrong input. Please enter yes or no: ").lower()

    if (play_again == "yes"):
        for key in board_keys:
            board[key] = " "

    else:
        break