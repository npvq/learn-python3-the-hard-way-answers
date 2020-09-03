people = 20
cats = 30
dogs = 15


if people < cats:
    print("Too many cats! The world is doomed!")

if people > cats:
    print("Not many cats! The world is saved!")

if people < dogs:
    print("The world is drooled on!")

if people > dogs:
    print("The world is dry!")


dogs += 5

if people >= dogs:
    print("People are greater than or equal to dogs.")

if people <= dogs:
    print("People are less than or equal to dogs.")


if people == dogs:
    print("People are dogs.")

# Study Drill Questions:
# 1. What do you think the if does to the code under it?
#    The if statement only executes the code underneath it when the granted
#    conditional statement has a boolean value of True.
# 2. Why does the code under the if need to be indented four spaces?
#    The code is signified to being part of the if statement when it is
#    indented four spaces. Otherwise the compiler will not execute it as part
#    of the if statement
# 3. What happens if it isn’t indented?
#    There is an IndentationError. That is, unless, the statement is two or
#    more lines away from the if statement, in which case it will be executed
#    by the compiler independently.
# 4. Can the other boolean expressions from Exercise 27 be in the if-statement?
#    Yes, as long as they output a True/False truth (boolean) value
# 5. What happens if you change the initial values for people, cats, and dogs?
#    Different conditional statements will be triggered and different
#    if-statements will be executed.
