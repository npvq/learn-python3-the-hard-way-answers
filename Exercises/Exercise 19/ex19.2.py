from sys import argv
from random import randint


# Define main function
def peanut_butter_jelly(bread_count, peanut_butter_count, jelly_count):
    # The following two variables are referenced many times, so I defined them
    # locally for more compact code.
    # Finds the minimum of the three values as integers
    min_pbjs = min(int(bread_count), int(peanut_butter_count), int(jelly_count)
                   )
    # Finds the maximum of the three values as integers
    max_pbjs = max(int(bread_count), int(peanut_butter_count), int(jelly_count)
                   )
    print(f"You have {int(bread_count)} slices of bread.")
    print(f"And you have {peanut_butter_count} servings of peanut butter and "
          f"{int(jelly_count)} servings of jelly.")
    print(f"Right now, you could make {min_pbjs} peanut butter jelly "
          "sandwiches.")
    # A bracket needs to envelop the integers in the operations.
    print(f"you will have {(int(bread_count) - min_pbjs)} loaves of "
          f"bread, {(int(peanut_butter_count) - min_pbjs)} servings of "
          f"peanut butter, and {(int(jelly_count) - min_pbjs)} servings "
          "of jelly left.")
    print(f"However, you could make {max_pbjs} peanut butter jelly "
          f"sandwiches if you had {(max_pbjs - int(bread_count))} more "
          f"loaves of bread, {(max_pbjs - int(peanut_butter_count))} "
          "more servings of peanut butter, and "
          f"{(max_pbjs - int(jelly_count))} more servings of jelly.\n")


# 1: Calling using argv modules
print("First, we will use the script's argv modules to call the function")
script, ex1_bread, ex1_peanut_butter, ex1_jelly = argv
peanut_butter_jelly(ex1_bread, ex1_peanut_butter, ex1_jelly)

# 2: Calling using input
print("Next, we will use user input to call the function")
prompt = "> "
print("Lets calculate how many peanut butter jelly sandwiches you could make!")
print("First, how many loaves of bread do you have?")
ex2_bread = int(input(prompt))
print("Next, how many servings of peanut butter do you have?")
ex2_peanut_butter = int(input(prompt))
print("Finally, how many servings of jelly do you have?")
ex2_jelly = int(input(prompt))

peanut_butter_jelly(ex2_bread, ex2_peanut_butter, ex2_jelly)


# 3: Calling using variables
print("Next, we will use variables to call the function")
ex3_bread = 25
ex3_peanut_butter = 21
ex3_jelly = 14
peanut_butter_jelly(ex3_bread, ex3_peanut_butter, ex3_jelly)


# 4: Calling directly using integers
print("Next, we will use numbers directly to call the function")
peanut_butter_jelly(36, 12, 24)


# 5: Calling directly using operations on integers
print("Next, we will use operations and numbers directly to call the function")
peanut_butter_jelly(12 * 2, 10 + 24, 55 - 36)


# 6: Calling using operations on variables
print("Next, we will use operations on only variables to call the function")
ex6_bread_debt = 9
ex6_peanut_butter_influx = 12
ex6_jelly_interest = 1.5
peanut_butter_jelly(ex3_bread - ex6_bread_debt, ex3_peanut_butter
                    + ex6_peanut_butter_influx, int(ex3_jelly
                                                    * ex6_jelly_interest))


# 7: Calling using operations on variables and integers
print("Next, we will use operations on integers and variables to call the "
      "function")
peanut_butter_jelly(17 - ex6_bread_debt, 48 + ex6_peanut_butter_influx, 26
                    * ex6_jelly_interest)


# 8: Calling using other functions
print("Next, we will use other functions to call the function")
ex8_bread = 19


def how_much_bread_today():
    return 45


def how_much_peanut_butter():
    return ex8_bread


def how_much_jelly():
    return input("How much jelly have you got there, mate?\n" + prompt)


peanut_butter_jelly(how_much_bread_today(), how_much_peanut_butter(),
                    how_much_jelly())


# 9: Calling using variables, integers, and user input
print("Next, we will use variables, integers, and user input directly to call "
      "the function")
peanut_butter_jelly(input("how much bread do we have?\n" + prompt),
                    ex3_peanut_butter, 25)


# 10: Calling using randomly generated numbers
print("Finally, we will use random numbers to call the function")
peanut_butter_jelly(randint(1, 101), randint(1, 101), randint(1, 101))

# This is based on the challenge to find 10 ways to call a function, using
# what we have learned so far. I chose not to use files for simplicity, as
# this is just an extension project.

# Warning: Scripts like these cannot be ran using IDLE properly,
# they are suited for the command line

# Usage Example: ex19.2.py 1 2 3
# Inputting anything other than numbers at any time will not work.
