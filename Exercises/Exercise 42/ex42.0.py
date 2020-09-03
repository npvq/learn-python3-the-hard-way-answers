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
    pass


# ?? <––(Salmon is-a Fish)
class Salmon(Fish):
    pass


# ?? <––(Hailbut is-a Fish)
class Hailbut(Fish):
    pass


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
flipper = Fish()

# ?? <––(crouse is-a Salmon)
crouse = Salmon()

# ?? <––(harry is-a Hailbut)
harry = Hailbut()


# In Python 3 you do not need to add the (object) after the name of the class,
# but the Python community believes in ”explicit is better than implicit”
# ”Python Zen says explicit is better than implicit.”
# Reference: https://www.python.org/dev/peps/pep-0020/
