# Defines the initial variables
people = 30
cars = 40
trucks = 15

# First if-statement: people and cars
if cars > people:
    # take the cars if there are more cars than people
    print("We should take the cars.")
elif cars < people:
    # don't take the cars if there are more people than cars
    print("We should not take the cars.")
else:
    # the exception being when there are as many people as cars
    # in which case a decision won't be able to be made
    print("We can't decide")

# Second if-statement: cars and trucks
if trucks > cars:
    # too many trucks if there are more trucks than cars
    print("That's too many trucks.")
elif trucks < cars:
    # plausible solution if there are less people than trucks
    print("Maybe we could take the trucks.")
else:
    # the exception being when there are as many cars as trucks
    # in which case a decision still won't be able to be made
    print("We still can't decide.")

# Third if-statement: people and trucks (+cars)
if people > trucks:
    # take the trucks if there are more people than trucks
    print("Alright, lets just take the trucks.")
elif people < cars:
    # ADDED: take the cars if there are too many trucks and still enough cars
    # ADDED: (more cars than people)
    print("Alright, lets just take the cars.")
elif people == cars and people == trucks:
    # ADDED: there will be hesitation if they are all the same
    print("What a coincidence! We can't choose at all.")
else:
    # ADDED: the exception being that neither worked out:
    # ADDED: too many trucks and not enough cars, won't be going out then.
    print("Way too many trucks, and not enough cars.")
    print("Fine, let's just stay home then.")

# elif: Else if; evaluates condition if preceding if/elif-statements are false
# else: Else; always executes if all adjoining if/elif-statements are false
# because "else" is always executed, it precedes no more conditional statemnets

# Python runs progressively through an if-statement and will execute the
#   actions under the first satisfied conditional and exit the if-statement.
