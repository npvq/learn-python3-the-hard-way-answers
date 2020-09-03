types_of_people = 10  # Sets the types of people for the string later
x = f"There are {types_of_people} types of people."  # Creates a format string

binary = "binary"  # Sets string variable to use later
do_not = "don't"  # Sets shorthand string variable to use later
y = f"Those who know {binary} and those who {do_not}"  # Formats a string

print(x)  # Prints string x
print(y)  # Prints string y

print(f"I said: {x}")  # Reitterates but with format
print(f"I also said \"{y}\"")  # Reitterates but with format

hilarious = False  # Sets booleen to format later
joke_evaluation = "Isn't that joke so funny?! {}"  # String w/ empty format

print(joke_evaluation.format(hilarious))  # Prints while formatting

w = "This is the left side of..."  # Create string
e = "a string with a right side."  # Creates another corresponding string

print(w + e)  # Prints while concatenating both strings using a plus operator


# There are (arguably) 5 places where a string was placed inside a string
# Lines 2, 6, 11, 12, 17_*
# *: Line 17 was a string that acted like a function because a variable was
# stored in it to format.
# in Line 22, a plus operator was used to concatenate two string variables.
