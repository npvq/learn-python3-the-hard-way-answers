# 1: Modules Are Like Dictionaries
# A module is: A Python file with some variables and functions
# You import that file and you can access these functions/variables via
# module with the . (dot) operator like: module.variable or module.function()

import ex40_mystuff  # Ignore PyCodeError for this line
mystuff = {'apple': "I AM APPLES!"}
print(mystuff['apple'])


# The following code has to be executed in the same directory as the script
# This goes in ex40_mystuff.py
module_commands = """
def apples():
    print("I AM APPLES!")


# this is just a variable
tangerine = "Living reflection of a dream"
"""

# Writes to ex40_mystuff.py (command from ex17.1.py)
exporting = open("ex40_mystuff.py", 'w+').write(module_commands)

ex40_mystuff.apples()

print(ex40_mystuff.tangerine)

# Common style in python:
# Take a key=value style container and get something out of it by the key name

# 2: Classes are like Modules
# A module is: A specialized dictionary that can store python code so you can
# access it with the . (dot) operator.


class MyStuff(object):

    def __init__(self):
        self.tangerine = "And now a thousand years between"

    def apple(self):
        print("I AM CLASSY APPLES!")


# 3: Objects are like Import
# If classes are like modules, objects are like imports.
# through a process called "instantiation" which is just fancy for 'to create'

thing = MyStuff()
thing.apple()
print(thing.tangerine)

# objects behave differently from modules, and this should only serve as a way
# for you to bridge over to understanding classes and objects.

# There are three ways to get things from things right now:
# dict style: mystuff['apples']
# module style: mystuff.apples(), print(mystuff.tangerine)
# class style: thing = MyStuff(), thing.apples(), print(thing.tangerine)

# Example Application:


class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)


happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"])

bulls_on_parade = Song(["There rally around tha family",
                        "With pockets full of shells"])


happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()


# More song lyrics

bohemian_rhapsody = Song(["Mama, just killed a man",
                          "Put a gun against his head",
                          "Pulled my trigger, now he's dead",
                          "Mama, life had just begun",
                          "But now I've gone and thrown it all away"])

twinkle_star_lyrics = ["Twinkle, Twinkle, bye bye Star",
                       "Soon to be no more, you are"]

twinkle_star = Song(twinkle_star_lyrics)

bohemian_rhapsody.sing_me_a_song()

twinkle_star.sing_me_a_song()
