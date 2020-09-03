# Defines the function
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    # Function cheese_and_crackers's actions
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enought for a party!")
    print("Get a blancket.\n")


print("We can just give the function numbers directly:")
# Calls function using integers as input/arguments
cheese_and_crackers(20, 30)


print("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

# Calls function using variabls as input/arguments
cheese_and_crackers(amount_of_cheese, amount_of_crackers)


print("We can even do math inside too:")
# Calls function using integers and operations inside the brackets as input
cheese_and_crackers(10 + 20, 5 + 6)


print("And we can combine the two, variables and math:")
# Calls function using variables, integers, and operations as input/arguments
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)


# In a way, the arguments to a function are kind of like our = character when
# we make a variable.
# If you can use = to name something, you can usually pass it to a function as
# an argument.
