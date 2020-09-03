# This code 'Magic 8 Ball' comes courtesy of PythonForBeginners:
# https://www.pythonforbeginners.com/code/magic-8-ball-written-in-python
# It has been converted to Python 3 using 2to3, refer to documentation below:
# https://docs.python.org/2/library/2to3.html
# And edited to follow the style guidelines of 'pycodestyle'

# Import the modules
import sys
import random

ans = True  # Sets a boolean value to variable ans

# This code could be improved by using "while True" as the variable 'ans' is
# not changed throughout the script
while ans:  # Main Module
    question = input("Ask the magic 8 ball a question: (press enter to quit) ")
    # Takes in user input

    answers = random.randint(1, 8)  # Randomly assigns an answer

    # This if statement exits the program if the answer is empty.
    if question == "":
        sys.exit()

    elif answers == 1:
        print("It is certain")

    elif answers == 2:
        print("Outlook good")

    elif answers == 3:
        print("You may rely on it")

    elif answers == 4:
        print("Ask again later")

    elif answers == 5:
        print("Concentrate and ask again")

    elif answers == 6:
        print("Reply hazy, try again")

    elif answers == 7:
        print("My reply is no")

    elif answers == 8:
        print("My sources say no")

    # No need for an else statement here.
    # randint(1, 8) will not return any other value than *range(1, 9)
