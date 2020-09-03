# Exercise 31 Extension: Write your own game using if-statments
# Monty Hall Game Show

import sys
from random import randint

door = str(randint(1, 3))

prompt = "> "


def kick_out():
    print("""Are you even trying to play the game?
If you don't want the Ferrari then others will take your place.

You have been kicked out of the game show for choosing a non-existent door.""")
    sys.exit("game terminated.")


def end_game(switch, win, guess, door):
    information = "Your final guess was Door {}, and the ferrari was behind \
door {}.".format(guess, door)
    if switch:
        if win:
            print(information)
            print("""Congratualtions on your win!
Changing your door gave you a 66.7% chance of winning! Smart move!""")
        else:
            print(information)
            print("""The odds weren't on your side this time.
Changing your door gave you a 66.7% chance of winning!
Outstanding move nonetheless!""")
    else:
        if win:
            print(information)
            print("""Lucky You! Your first guess was correct!
Keeping your choice only gave you a 33.3% chance of winning.
Don't be proud yet, and remember that when playing like this the odds are \
always stacked against you""")
        else:
            print(information)
            print("""Bad move! Your first guess was incorrect.
Keeping your choice only gave you a 33.3% chance of winning.
Ruminate on your failures and figure out why you get twice the chance of \
winning a Ferrari by switching doors.""")


print("""Welcome to the Monty Hall game show!
YOU have been selected to play the game
Press RETURN to continue.""")

input(prompt)

print("""The rules are as follows:
there are three doors
entitles door 1, door 2, and door 3.
Behind two doors are life-sized participation awards
and Behind the other one is a Ferrari

You have to first make a guess on which door might hold the mighty prize:
[1] Door 1, [2] Door 2, [3] Door 3.""")

guess = input(prompt)
global open  # <–– Apparently this is very bad practice, I'll have to look out

if guess == door:
    unchosen = ["1", "2", "3"]
    unchosen.remove(guess)
    chance = randint(0, 1)
    open = unchosen[chance]

elif guess == "1" or (guess == "2" or guess == "3"):
    if not (guess == "1" or door == "1"):
        open = "1"
    elif not (guess == "2" or door == "2"):
        open = "2"
    elif not (guess == "3" or door == "3"):
        open = "3"
    print()

else:
    kick_out()


print(f"You have chosen door {guess}\nAnd Monty Hall suddenly walked towards \
door number {open} and opened it to reveal a participation award")
print("""Now, he gives you the choice to either keep your guess
or switch your guess to the other door.
Would you like to switch your door?

[Y]es [N]o""")

switch = input(prompt)

if switch == "Y" or switch == "y":
    if guess == door:
        unchosen = ["1", "2", "3"]
        unchosen.remove(guess)
        unchosen.remove(open)
        other = unchosen[0]
        end_game(True, False, other, door)
    else:
        print(f"You switched from Door {guess} to Door {door}")
        end_game(True, True, guess, door)

elif switch == "N" or switch == "n":
    if guess == door:
        print(f"You kept your choice of Door {guess}")
        end_game(False, True, guess, door)
    else:
        print(f"You kept your choice of Door {guess}")
        end_game(False, False, guess, door)

else:
    kick_out()

# Debugging note: Initially, there were discreptancies between comparing type
# Str and type Int, which caused weird bugs in the if statements
# Also, randint(a, b) chose between [a, b] and not [a-1, b-1].
