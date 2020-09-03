# You can use indices to get stored data from lists like list[index]
# However, you can only use numbers (integers) to get things from lists
# On the other hand, you can associate *Anything* to another with a Dictionary.
# Dictionaries are like "look-up tables"

# Note: A set is a list without order/indexing

# creates a mapping of state to abbreviation
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

# create a basic set of states and some cities in them
cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

# add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print out some cities
print('-' * 10)
print("NY State has: ", cities['NY'])
print("OR state has: ", cities['OR'])

# print some states
print('-' * 10)
print("Michigan's abbreviation is: ", states['Michigan'])
print("Florida's abbreviation is: ", states['Florida'])

# do it by using the state then cities dict
print('-' * 10)
print("Michigan has: ", cities[states['Michigan']])
print("Florida has: ", cities[states['Florida']])

# print every state abbreviation
print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated {abbrev}")

# print every city in states
print('-' * 10)
for abbrev, city in list(cities.items()):
    print(f"{abbrev} has the city {city}")

# now do both at the same time
print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} state is abbreviated {abbrev}")
    print(f"and has city {cities[abbrev]}")

print('-' * 10)
# safely get an abbrevaition by state that might not be there
state = states.get('Texas')
if not state:
    print("Sorry, no Texas.")

# get a city with a default value
city = cities.get('TX', 'Does Not Exist')
print(f"The city for the state 'TX' is: {city}")

# Study Drills:
# (1) Idea for upcoming project.

# Python Documentation for Dictionaries
# Reference: https://docs.python.org/3/tutorial/datastructures.html
# Dictionaries can be set/accessed as follows: dictionary[key] = value

# The dict() command can construct dictionaries as such:
#       example: dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
# sometimes (for simple dictionaries) it is simpler to specify pairs with
# keyword arguments.
#       example: dict(sape=4139, guido=4127, jack=4098)

# del dictionary[keyword] removes the pair {keyword: value} from dictionary
# len(dictionary) returns the number of keyword-value pairs
# x in dictionary = True when x is a key in the dictionary

# refer to dictoinary methods (CSV) file. Reference for CSV file below:
# https://www.w3schools.com/python/python_ref_dictionary.asp

# Dictionary Advantages and Disadvantages:
# Advantage: It improves the readability of your code.
# Advantage: You can look up a key in a Python dictionary very fast.
#            (As compared to iterating through lists)
# Disadvantage: Dictionaries are unordered.
#               (do not use dictionaries if you need ordered data)
# Disadvantage: Python dictionaries take up a lot more space than other data
#               structures. (but that's usually fine)

# dictionaries can be used for more efficient Memo as in the following example
# ref: http://openbookproject.net/thinkcs/python/english3e/dictionaries.html

alreadyknown = {0: 0, 1: 1}


def fib(n):
    if n not in alreadyknown:
        new_value = fib(n-1) + fib(n-2)
        alreadyknown[n] = new_value
    return alreadyknown[n]


print(fib(100))

# This is much more efficient compared to individually calling itself
# recursively, so each function is only called *once*.
