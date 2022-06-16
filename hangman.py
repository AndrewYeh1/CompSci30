# Andrew Yeh
# Hangman
# CompSci 30
# Sept 23rd
# This program is my own work - A.Y.

import random


def input_letter(letters):
    ret = input("Enter a letter to guess: ")
    while ret in letters or len(ret) != 1 or ret not in "abcdefghijklmnopqrstuvwxyz":
        ret = input("Invalid, try again: ")
    return ret


def print_hangman(letters, word):
    numTries = 0
    for x in letters:
        if x not in word:
            numTries += 1
            print(x, end=" ")
    print()
    win = True
    for x in word:
        if x in letters:
            print(x, end=" ")
        else:
            print("-", end=" ")
            win = False
    print(hangman_pics[numTries])
    if win:
        return -1
    else:
        return numTries


hangman_pics = ['''
 +---+
     |
     |
     |
    ===''', '''
 +---+
 O   |
     |
     |
    ===''', '''
 +---+
 O   |
 |   |
     |
    ===''', '''
 +---+
 O   |
/|   |
     |
    ===''', '''
 +---+
 O   |
/|\  |
     |
    ===''', '''
 +---+
 O   |
/|\  |
/    |
    ===''', '''
 +---+
 O   |
/|\  |
/ \  |
    ===''']
words = ["apple", "banana", "orange", "grape", "watermelon", "pear", "peach"]

play = True

while play:
    print("Your category is fruits.")

    num = random.randint(0, 6)

    tries = 0
    letterList = []
    while 5 > tries:
        tries = print_hangman(letterList, words[num])
        if tries == -1:
            break
        letterList.append(input_letter(letterList))
    if tries == 5:
        print_hangman(letterList, words[num])
        print("You failed.")
    else:
        print("You win.")
    print("The word was:", words[num] + ".")
    play = input("Play again? (y or n): ")
    while play != "y" and play != "n":
        play = input("Invalid. (y or n): ")
    if play == "n":
        play = False
