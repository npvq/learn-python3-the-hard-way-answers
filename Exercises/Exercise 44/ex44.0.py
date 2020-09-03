# REMEMBER: Most of the uses of inheritance can be simplified or replaced with
# composition, and multiple inheritance should be avoided at all costs.

# Parent and Child classes.
# When you say: class Foo(Bar), or "Make a class Foo that inherits from Bar."
# and action that you do on instances of Foo will work as if they were done to
# This way, you can put common functionality in Bar
# And specific specialized functionality in Foo later.

# There are three ways Parent and Child classes can interact.
# 1: Implicit Inheritance


class Parent1(object):

    def implicit(self):
        print("PARENT implicit()")


class Child1(Parent1):

    pass  # <–– specifies an empty block without raising errors
    # Useful if you want to test it now and fill it in later


dad1 = Parent1()
son1 = Child1()

dad1.implicit()  # <–– (Returns "PARENT implicit()")
son1.implicit()  # <–– (Returns "PARENT implicit()")

# if you put functions in a base class (i.e., Parent), then all subclasses
# (i.e., Child) will automatically get those features.
# Very handy for repetitive code you need in many classes.

# 2: Override Explicitly


class Parent2(object):

    def override(self):
        print("PARENT override()")


class Child2(Parent2):

    def override(self):
        print("CHILD override()")


dad2 = Parent2()
son2 = Child2()

dad2.override()  # <–– (Returns "PARENT override()")
son2.override()  # <–– (Returns "CHILD override()")

# If child ought to behave differently than parent, you can define the function
# of the same name again inside child, which will effectively override its
# parent class's function

# 3: Alter Before and After:


class Parent3(object):

    def altered(self):
        print("PARENT altered()")


class Child3(Parent3):

    def altered(self):
        print("CHILD, BEFORE PARENT altered()")
        super(Child3, self).altered()
        # ”call super with arguments Child and self,
        #  then call the function altered on whatever it returns.”
        print("CHILD, AFTER PARENT altered()")


dad3 = Parent3()
son3 = Child3()

dad3.altered()  # <–– (Returns "PARENT altered()")
son3.altered()  # <–– (Returns "CHILD, BEFORE PARENT altered()"
#               #              "PARENT altered()"
#               #              "CHILD, AFTER PARENT altered()")

# with this (using super), the child can choose to perform whatever actions
# before and whatever actions after calling the parent equivalent function.
