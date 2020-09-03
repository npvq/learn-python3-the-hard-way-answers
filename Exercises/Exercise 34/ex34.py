# Because programmers do not rely on the intuitive ordinal numbers
# (think order), their best way of indexing starts at 0.
# Remember: ordinal == ordered, 1st; cardinal == cards at random, 0.

animals = ['bear', 'python3.6', 'peacock', 'kangaroo', 'whale', 'platypus']

# 1: The animal at 1.
animals[1]  # @ 1 and is python3.6
# 2: The third (3rd) animal.
animals[2]  # @ 2 and is peacock
# 3: The first (1st) animal.
animals[0]  # @ 0 and is bear
# 4: The animal at 3.
animals[3]  # @ 3 and is kangaroo
# 5: The fifth (5th) animal.
animals[4]  # @ 4 and is whale
# 6: The animal at 2.
animals[2]  # @ 2 and is peacock
# 7: The sixth (6th) animal.
animals[5]  # @ 5 and is platypus
# 8: The animal at 4.
animals[4]  # @ 4 and is whale

# Study Drill 1: The year 2010 is not actually 2009 because years are ordinal
# numbers that succeed themselves every time the Earth makes a full revolution
# around the sun.
# Study Drill 2: Translate more indices (fruits list from ex32.py)

fruits = ['apples', 'oranges', 'pears', 'apricots']

# This for loop could be used on lists of any size.
# len(x) returns the integer size (number of indices) of the list x.
print("List of fruits: ", fruits)
for i in range(0, len(fruits)):
    print("The {}st fruit, at index {}, is {}".format((i + 1), i, fruits[i]))
