ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("Wait there are not 10 things in that list. Let's fix that.")

stuff = ten_things.split(' ')
# "Call split on 10 things using space"
# split(ten_things using ' '), "Call split with arguments 10 things and space"
more_stuff = ["Day", "Night", "Song", "Frisbee",
              "Corn", "Banana", "Girls", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    # "Call pop on more_stuff"
    # pop(more_stuff) "Call pop with argument more_stuff"
    print("Adding: ", next_one)
    stuff.append(next_one)
    # "Call append on stuff with argument next_one"
    # append(next_one to stuff) "Call append with arguments stuff and next_one"
    print(f"There are {len(stuff)} items now")
    # len(stuff), "call len with argument stuff"

print("There we go: ", stuff)

print("Let's do some things with stuff.")

print(stuff[1])
print(stuff[-1])  # whoa! fancy
print(stuff.pop())
print(' '.join(stuff))  # what? cool!
# "Call join on ' ' with argument stuff"
# join(' ', stuff) <–– Doesn't work "Call join with arguments space and stuff"
print('#'.join(stuff[3:5]))  # super stellar!
# That [3:5] works similarly to range(3, 5) but wiht indices

# Refer to ex22.py for list commands

# Example of things that would fit in a list:
list_examples = ["Types of Coffee", "Deck of Cards", "Directory Names/Paths",
                 "Contacts", "Game Inventory", "Image Viewing", "Music Player",
                 "Web Browse Previous/Next Page", "Matrices", "Complex Algebra"
                 ]
# Ref:https://www.geeksforgeeks.org/applications-of-linked-list-data-structure/
# Class: https://docs.python.org/3.3/tutorial/classes.html 9.3.2 Class Objects


# Examples of class definition:
class MyClass:
    """A simple example class"""
    i = 12345  # A class can have variables

    def f(self):  # And a class can have functions
        return 'hello world'


print(MyClass.i)
example = MyClass()  # Class definitions are called like functions
print(example.i, "==", MyClass.i)
example.f()  # should return "hello world"

# Classes use __init__() to instantiate content inside the class definition
# Example of class instantiation:


class Complex:
    def __init__(self, realpart, imagpart):  # Real and Imaginary parts
        self.r = realpart
        self.i = imagpart


# This basically lets you "call" classes

number = Complex(3.0, 4.5)

print("the answer is {} + {}i".format(number.r, number.i))

# When to use lists:
# 1. If you need to maintain order. Remember, this is listed order, not sorted
#    order. Lists do not sort for you.
# 2. If you need to access the contents randomly by a number. Remember, this is
#    using cardinal numbers starting at 0.
# 3. If you need to go through the contents linearly (first to last). Remember,
#    that’s what for-loops are for.


# Object Oriented Python Programming (OOP):

# - A programming paradigm which provides a means of bundling attributes and
#   behaviors into _objects_
# Attributes like Variables and Behaviors like Functions

# - Put another way, object-oriented programming is an approach for modeling
#   concrete, real-world things
# Example: an Emails have attributes such as recipient list, subject, body,
# etc., and behaviors like adding attachments and sending.

# Another common programming paradigm is procedural programming which
# structures a program like a recipe in that it provides a set of steps, in the
# form of functions and code blocks, which flow sequentially in order to
# complete a task.

# The key takeaway is that objects are at the center of the object-oriented
# programming paradigm in the overall structure of the program.

# Reference: https://realpython.com/python3-object-oriented-programming/
