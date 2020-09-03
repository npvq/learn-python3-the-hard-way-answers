# This code 'Pig Latin Translator' comes courtesy of Python Fiddle:
# http://pythonfiddle.com/pig-latin-translator-for-python/
# It has been converted to Python 3 using 2to3, refer to documentation below:
# https://docs.python.org/2/library/2to3.html
# And edited to follow the style guidelines of 'pycodestyle'

# Take the users input
words = input("Enter some text to translate to pig latin: ")
print("You entered: ", words)

# Now I need to break apart the words into a list
words = words.split(' ')

# Now words is a list, so I can manipulate each one using a loop

for i in words:
    if len(i) >= 3:  # I only want to translate words greater than 3 characters
        i = i + "%say" % (i[0])
        i = i[1:]
        print(i)
    else:
        pass
