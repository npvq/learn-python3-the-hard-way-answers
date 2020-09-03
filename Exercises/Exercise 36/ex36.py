# Game: Space Travel Problems
from sys import exit

prompt = "> "


def start():
    print("""Click. Clack.
You find yourself awakened to the rustling sounds of a roaring sandstorm"""
          + """ outside.
You scramble to find your watch as you hopped out of the space travel pod.
The clock, functioning on weird quantum properties that even you don't """
          + "understand, had somehow kept the time accurately while you were "
          + """in hibernation.
The day is Friday, March 14th, 2797.
As the realization that you are now in the middle of nowhere..
600 years after your departure..
dawned on you, you quickly scramble to check your cockpit control panel.""")
    print("press RETURN to continue")
    input()
    cockpit(False, 5)


# Cockpit is the first room of the game, it is repeatable; there will be
# another script to start.
# fuel is a Boolean for fuel or no fuel and HP is an integer.
def cockpit(fuel, HP):
    if not fuel:
        if HP < 1:
            death("the lack of food")

        print("Cockpit:")
        print("FUEL EXTREMELY LOW, CANNOT TAKE OFF")
        print(f"You have supplies to sustain for approximately {HP} days\n")
        print("Current Environment:\nTemperature: 300 Kelvins\nAtmospheric \
Pressure: 97.8 Pa\nAtmosphere: 55% Nitrogen, 27% Oxygen, 9% Hydrogen, 5% \
Helium\nComment: Weirdly Similar to Earth's Atmostphere!")
        print("\n\nwhat do you want to do?")
        print("[1] Stay Inside No Matter What\n[2] Go Outside\n[3] Call the \
Interstellar Emergency Aid (IEA)")
        choice = input(prompt)
        if choice == "1":
            print("""You were certain that no matter how urgent the situation..
You won't give up playing tap tap heroes and smashing those "online" bots""")
            death("the lack of willpower")
        elif choice == "2":
            print("""You take a deep breath as you open up the cockpit doors..
It turns out that your Cockpit AI was correct,
this place DID have similar climates to the Earth's,
except for the abrasive crystals of hematite and silica..
soaring in the winds betwixt the collosal deserty biome.\n\n""")
            dirt(HP)
        elif choice == "3":
            print("\nYou desperately started the Interstellar Communications "
                  + """Unit on your ship and started transmitting.
>>>SOS! R=102.77934105 parsecs, θ=71.92801947º ¡SOS>>>
The typical stuff.
But you are subtly unsure whether the signal frequencies have changed..
After all, you haven't communicated with the IEA for the past six centuries..
But it's still helpful have faster-than-light communications..
using quantum entanglement, you thought.""")
            print("\n...a full day passed and no response")
            print("you start to question whether the IEA still exists.\n")
            cockpit(fuel, (HP - 1))
        else:
            print("Your entry was invalid, please submit a valid entry.")
            print("!Hint: type the option/numbers to the left.\n")
            cockpit(fuel, HP)
    else:
        print("With your new battery installed, you are ready to take off.")
        print("Then, you started pondering yet another question.")
        print("Where will you go now? It's not like you have any friends to \
go visit.\n")
        print("CONGRATULATIONS ON WINNING THE GAME")


# The second room of the game, and the only room to go from the cockpit.
# This room will not be accessed when fuel=True, which goes directly to cockpit
def dirt(HP):
    print("""The desert is vast and empty..
the only entities that you could make out with your eyes..
while being constantly bombarded by the sand..
are a small hut nearby and a Mountain in the distance.""")
    print("\n\nWhere would you like to go?")
    print("[1] Mountain\n[2] The Small Hut")
    choice = input(prompt)
    if choice == "1":
        print("You stride towards the mountain, it was a long walk.\n\n")
        mountain(HP)
    elif choice == "2":
        print("You stroll towards the hut, it was a short walk.\n\n")
        hut(HP)
    else:
        print("Your entry was invalid, please submit a valid entry.")
        print("!Hint: type the option/numbers to the left.\n")
        dirt(HP)


# This room is accessible through "Dirt"
def mountain(HP):
    print("Upclose, the summit was so tall that it was almost out of vision.")
    print("However, down at the bottom is a modest cave, "
          + "What could possibly be there?")
    print("\n\nWhere would you like to go?")
    print("[1] Summit\n[2] Cave")
    choice = input(prompt)
    if choice == "1":
        print("You set off to a long climb.\n.\n.\n.")
        print("You start to feel your back heating up, and your perspiration \
comes to a halt. You now feel very dehydrated.")
        print("Not long after, you arrived at the top of the mountain.")
        print("To your suprise, there was nothing, and there was your life \
destiny")
        death("excessive solar radiation")
    elif choice == "2":
        print("You take a breath and walk into the cave.\n\n")
        cave(HP)
    else:
        print("Your entry was invalid, please submit a valid entry.")
        print("!Hint: type the option/numbers to the left.\n")
        mountain(HP)


# This room is accessible through "Mountain", returns player to "Dirt"
def cave(HP):
    print("The adit of the cave was snug and cozy, inside which sits a giant \
bear, sipping his coffee and sitting on a... WAIT...")
    print("He is sitting on a Antimatter Fuel Battery, exactly what you need \
to power your spaceship.")
    print("\n\nWhat will you do?")
    print("[1] Flee\n[2] Fight\n[3] Sneak to the battery")
    choice = input(prompt)
    if choice == "1":
        print("You turn around and sprint away without second thoughts.")
        print("As if it was second nature, you ran for hours without looking \
back")
        print("Finally, your cockpit is in sight again.")
        print("You turn back and there bear hasn't followed you back")
        print("Smart move! Hope you've learned your lesson and won't go back \
to the cave again.\n\n")
        dirt(HP)
    elif choice == "2":
        print("You know how this would go. The self-proclaimed WWE fighter \
fails to beat the 400-pound furry beast, and becomes human toast to \
complement the bear's morning coffee")
        death("a giant bear")
    elif choice == "3":
        print("You slowly sneak behind the bear, while trying to catch your \
breath. Your detective hobbies have really payed off.")
        print("But you quickly arrive at your next obstacle: How in the world \
are you going to get that battery from underneath a 400-pound beast?")
        print("just as your thought process caught up, The bear looks at you \
then slaps your face off.")
        death("a giant bear")
    else:
        print("Your entry was invalid, please submit a valid entry.")
        print("!Hint: type the option/numbers to the left.\n")
        cave(HP)


# This room is accessible through "Dirt" and leads back to "Cockpit"
def hut(HP):
    print("After you made your way to the hut, you find that its owner is a \
friend alien with a strange passion")
    print("After you explained your situation, he is willing to offer you \
some help, but he first explains that there is a math problem that he \
cound't figure out and has been bothering him.")
    print("He couldn't figure out what 1010! is")
    print("And he is willing to offer you his only spare Antimatter battery \
if you are able to solve it correctly.")
    print("\n\nwhat do you want to do?")
    print("[tip]: Your alien friend only has one finger on each hand")
    print("[1] Help Him Solve\n[2] Ignore")
    choice = input(prompt)
    if choice == "1":
        print("\n\n>>>What is 1010!")
        answer = input(prompt)
        if answer == "1101110101111100000000":
            print("\n\n" + f"[{answer}]")
            print("Wow! Your alien friend is amazed at your ability to solve \
it so quickly. Even though he has no idea whether you got it right, he gave \
you his battery as a gift of appreciation")
            print("You thank him as you head back to the cockpit.\n\n")
            cockpit(True, HP)
        else:
            print("Before you could think of where you went wrong with that \
answer, a giant bear attacked you from behind, you are a piece of toast.")
            death("an ambush by a giant bear")
    elif choice == "2":
        print("You turned down his offer becuase you absolutely abhor \
anything related to math. What a waste of time. You wasted the whole day \
before returning to the cockpit\n\n")
        cockpit(False, (HP - 1))
    else:
        print("Your entry was invalid, please submit a valid entry.")
        print("!Hint: type the option/numbers to the left.\n")
        hut(HP)


# This deals with death messages and exits the script when called.
def death(reason):
    print("\n>>>You have succumbed to", reason)
    exit(0)


# Main Loop starts here
start()

# Answer: 10! (1010!) = 3,628,800 (1101110101111100000000) Binary

# Description: This script works by breaking down the various rooms into
# functions that can be called individually. The functions all pass on a
# paramenter entitled "HP" to one another, eliminating a need to use a
# gobal (error-prone) way to keep track of health-points.
# These concepts are worth noting when experimenting with more sophisticated
# concepts.
