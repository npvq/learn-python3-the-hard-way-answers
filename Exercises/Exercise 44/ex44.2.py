# COMPOSITION
# Inheritance is useful, but another way to do the exact same thing is just to
# use other classes and modules, rather than rely on implicit inheritance.
# If you look at the three ways to exploit inheritance, two of the three
# involve writing new code to replace or alter functionality. This can easily
# be replicated by just calling functions in a module.


class Other(object):

    def override(self):
        print("OTHER override()")

    def implicit(self):
        print("OTHER implicit()")

    def altered(self):
        print("OTHER altered()")


class Child(object):

    def __init__(self):
        self.other = Other()

    def implicit(self):
        self.other.implicit()

    def override(self):
        print("CHILD override()")

    def altered(self):
        print("CHILD, BEFORE OTHER altered()")
        self.other.altered()
        print("CHILD, AFTER OTHER altered()")


son = Child()
son.implicit()
son.override()
son.altered()

# This time, Child != is-a Parent. Instead, it's using Child has-a Other to get
# the work done.
# most of the code in Child and Other is the same to accomplish the same thing.
# The only difference is that I had to define a Child.implicit function to do
# that one action. Does Other to be a class, or could I just make it into a
# module named other.py?

# When to Use Inheritance or Composition?
# Both of them are used to make code cleaner, reusable, and more efficient.
# Guidelines:

"""
1. Avoid multiple inheritance at all costs, as it’s too complex to be reliable.
If you’re stuck with it, then be prepared to know the class hierarchy and spend
time finding where everything is coming from.

2. Use composition to package code into modules that are used in many different
unrelated places and situations.

3. Use inheritance only when there are clearly related reusable pieces of code
that fit under a single common concept or if you have to because of something
you’re using.
"""

# Style Guide: https://www.python.org/dev/peps/pep-0008/
