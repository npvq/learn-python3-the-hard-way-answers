# This code 'Hangman' comes courtesy of PythonForBeginners:
# https://www.pythonforbeginners.com/code-snippets-source-code/game-hangman/
# It has been converted to Python 3 using 2to3, refer to documentation below:
# https://docs.python.org/2/library/2to3.html
# And edited to follow the style guidelines of 'pycodestyle'

# importing the time module
import time

# welcoming the user
name = input("What is your name? ")  # Fixed undefined function name
# system built-in input() and not raw_input()

print("Hello, " + name, "Time to play hangman!")

print("\n")

# wait for 1 second
time.sleep(1)

print("Start guessing...")
time.sleep(0.5)

# here we set the secret
word = "secret"

# creates an variable with an empty value
guesses = ''

# determine the number of turns
turns = 10

# Create a while loop

# check if the turns are more than zero
while turns > 0:

    # print the attempt number if it's not the first turns
    if not turns == 10:

        print("Attempt {}: ".format(str(10 - turns)), end='')

    # make a counter that starts with zero
    failed = 0

    # for every character in secret_word
    for char in word:

        # see if the character is in the players guess
        if char in guesses:

            # print then out the character
            print(char, end='')  # Fixed end='' syntax

        else:

            # if not found, print a dash
            print("_", end='')  # Fixed end='' syntax

            # and increase the failed counter with one
            failed += 1

    # print a newline
    print("\n")

    # if failed is equal to zero

    # print You Won
    if failed == 0:
        print("\nYou won")

        # exit the script
        break

    print

    # ask the user go guess a character
    guess = input("guess a character:")  # fixed 'input()'

    # if the guess is not found in the secret word
    if guess not in word:

        # turns counter decreases with 1 (now 9)
        turns -= 1

        # print wrong
        print("Wrong\n")

        # how many turns are left
        print("You have", + turns, 'more guesses')

        # if the turns are equal to zero
        if turns == 0:

            # print "You Lose"
            print("You Lose\n")

    # then if player's guess is not already in guesses
    elif guess not in guesses:

        # set the players guess to guesses
        guesses += guess

    # If the word is already guessed
    else:

        # print messages
        print("You have already guessed that!")

# Fixed all newline escape codes
