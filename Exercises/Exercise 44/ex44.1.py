# INHERITANCE Example:


class Parent(object):

    def implicit(self):
        print("PARENT implicit()")

    def override(self):
        print("PARENT override()")

    def altered(self):
        print("Parent altered()")


class Child(Parent):

    def override(self):
        print("CHILD override()")

    def altered(self):
        print("CHILD, BEFORE PARENT altered()")
        super(Child, self).altered()
        print("CHILD, AFTER PARENT altered()")


dad = Parent()
son = Child()

print("Implicit:")
dad.implicit()
son.implicit()
print('-' * 10)

print("Override:")
dad.override()
son.override()
print('-' * 10)

print("Altered:")
dad.altered()
son.altered()

# Why we need super():
# In multiple inheritance, python needs to resolve an order (called MRO)
# of which base classes to check first, super() can modify that.

# still, it's main use is with the __init__() function
# when you have to initiate and do something in the child class first
# before going on to finish the parent class initiation. Example:


class Number():  # Bass Class

    def __init__(self, number):
        self.number = number


class Square(Number):  # Subclass

    def __init__(self, number):
        self.value = number
        sqrt = number ** 0.5
        super(Square, self).__init__(sqrt)


hundred = Square(100.0)
print(hundred.value)
print(hundred.number)
