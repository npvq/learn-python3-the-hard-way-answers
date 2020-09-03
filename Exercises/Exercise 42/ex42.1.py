# A salmon is a kind of fish.
# And Mary is a salmon.
# Neither fish nor salmon are real, they are just classes that we attribute to
# entities that have specific attributes.
# But Mary was created from fish, she is an instance of a salmon and of a fish.
# So Mary is a salmon that is a kind of fish––object is a class is a class.


# Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal (object):
    pass  # acts as a placeholder for functions/conditionals/loops/classes


# ?? <––(Dog is-a(n) Animal)
class Dog(Animal):

    def __init__(self, name):
        # ?? <––(Dog has-a name)
        self.name = name


# ?? <––(Cat is-a(n) Animal)
class Cat(Animal):

    def __init__(self, name):
        # ?? <––(Cat has-a name)
        self.name = name


# ?? <––(Person is-a object)
class Person(object):

    def __init__(self, name):
        # ?? <––(Person has-a name)
        self.name = name

        # Person has-a pet of some kind (has to be manually assigned)
        # This defaults to None
        self.pet = None


# ?? <––(Employee is-a Person)
class Employee(Person):

    def __init__(self, name, salary):
        # ?? hmm what is this strange magic?
        super(Employee, self).__init__(name)
        # ?? <––(Employee has-a salary)
        self.salary = salary


# ?? <––(Fish is-a object)
class Fish(object):

    def __init__(self, name):
        self.name = name

    def description(self):
        print(f"{self.name} is a Fish")


# ?? <––(Salmon is-a Fish)
class Salmon(Fish):

    def __init__(self, name):
        super(Salmon, self).__init__(name)  # Inherits self.name

    def description(self):
        print(f"{self.name} is a Salmon")
        super().description()

    def accessSalmon(self):
        print(f"{self.name} has a Salmon passport")


# ?? <––(Hailbut is-a Fish)
class Hailbut(Fish):

    def __init__(self, name):
        super(Hailbut, self).__init__(name)  # Inherits self.name

    def description(self):
        print(f"{self.name} is a Hailbut")
        super().description()

    def accessHailbut(self):
        print(f"{self.name} has a Hailbut passport")


class Hybrid(Salmon, Hailbut):

    def __init__(self, name):
        super(Hybrid, self).__init__(name)  # Inherits self.name

    def description(self):
        print(f"{self.name} is a Hybrid!")
        super().description()


# rover is-a dog
rover = Dog("Rover")

# ??  <––(satan is-a Cat)
satan = Cat("Satan")

# ??  <––(mary is-a Person)
mary = Person("Mary")

# ??  <––(mary has-a Pet (Cat) satan)
mary.pet = satan

# ?? <––(frank has-a salary of 120000)
frank = Employee("frank", 120000)

# ?? <––(frank has-a Pet (Dog) rover)
frank.pet = rover

# ?? <––(flipper is-a Fish)
flipper = Fish('Flipper')
flipper.description()
print('-' * 10)

# ?? <––(crouse is-a Salmon)
crouse = Salmon('Crouse')
crouse.description()
crouse.accessSalmon()
print('-' * 10)

# ?? <––(harry is-a Hailbut)
harry = Hailbut('Harry')
harry.description()
harry.accessHailbut()
print('-' * 10)

weirdo = Hybrid('Weirdo')

weirdo.description()
weirdo.accessSalmon()
weirdo.accessHailbut()

# In Python 3 you do not need to add the (object) after the name of the class,
# but the Python community believes in ”explicit is better than implicit”
# ”Python Zen says explicit is better than implicit.”

# Study Drills:

# Firsty, everything is an object: lists, strings, integers, anything.

# The object() function returns an empty object. You cannot add new properties
# or methods to this object. This object is the base for all classes, it holds
# the built-in properties and methods which are default for all classes.
# Reference: https://www.w3schools.com/python/ref_func_object.asp

# Like C++, a class can be derived from more than one base classes in Python.
# This is called multiple inheritance.
# In multiple inheritance, the features of all the base classes are inherited
# into the derived class. The syntax for multiple inheritance is similar to
# single inheritance.
# Example: class Base1(object); class Base2(object); class multi(Base1, Base2).
# Reference: https://www.programiz.com/python-programming/multiple-inheritance
# It is frowned upon because inheriting from multiple objects means inheriting
# all of their dependencies, both implicit and explicit.
# And usually, that isn't true.
# Reference: https://softwareengineering.stackexchange.com/questions/218458/
#            is-there-any-real-reason-multiple-inheritance-is-hated

# Super() Allows us to avoid using the base class name explicitly
# We can use super to reference/initiate base classes.
# It can also help us deal with multiple inheritance.
# super().__init__(parameters) initiates the base category
# super(x, self) initiates the parent category of x with self.
# Reference: https://realpython.com/python-super/
