from sys import exit

prompt = "> "


# In all of the scenarios, you may die for doing the wrong thing.
# This is the Gold Room scenario, it does not lead to any other scenario/branch
def gold_room():
    print("This room is full of gold. How much do you take?")

    choice = input(prompt)
    # The best way to evaluate whether user input is a integer without using
    # ValueError is via the .isdigit() command of a variable of type str.
    if choice.isdigit():
        how_much = int(choice)
    else:
        dead("Man, learn to type a number.")

    if how_much < 50:
        print("Nice, you're not greedy, you win!")
        exit(0)
    else:
        dead("You greedy bastard!")


# This is the Bear Room scenario, it can lead to Gold Room.
def bear_room():
    print("There is a bear here.")
    print("The bear has a bunch of honey.")
    print("The fat bear is in front of another door.")
    print("How are you going to move the bear.")
    bear_moved = False

    while True:
        choice = input(prompt)

        if choice == "take honey":
            dead("The bear looks at you then slaps your face off.")
        elif choice == "taunt bear" and not bear_moved:
            print("The bear has moved from the door.")
            print("You can go through it now.")
            bear_moved = True
        elif choice == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
        elif choice == "open door" and bear_moved:
            gold_room()
        else:
            print("I got no idea what that means.")


# This is the Cthulhu Room scenario, it can lead back to the start room
def cthulhu_room():
    print("Here you see the great evil Cthulhu.")
    print("He, it, whatever stares at you and you go insane.")
    print("Do you flee for your life or eat your head?")

    choice = input(prompt)

    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("Well that was tasty!")
    else:
        print("Are you going crazy?")
        cthulhu_room()


# This is the Death Scenario, it takes a prompt and exits/breaks the script
def dead(why):
    print(why, "Good job!")
    print("YOU HAVE DIED.")  # <–– Added for clarity.
    exit(0)


# This s the Start Room scenario, it leads to either the Bear Room or the
# Cthulhu Room.
def start():
    print("You are in a dark room.")
    print("There is a door to your right and a door to your left.")
    print("Which one do you take")

    choice = input(prompt)

    if choice == "left":
        bear_room()
    elif choice == "right":
        cthulhu_room()
    else:
        dead("You stumble around the room until you starve.")


start()

# A game flow chart depicting the routes taken by the player can be found at
# ex35_game_flow.png

# "The operators "in" and "not in" test for collection membership.  "x in s"
#  evaluates to true if *x* is a member of the collection *s*, and false
#  otherwise. For the list and tuple types, "x in y" is true if and only if
#  there exists an index *i* such that "x == y[i]" is true." -pydoc
