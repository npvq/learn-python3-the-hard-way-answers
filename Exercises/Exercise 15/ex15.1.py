# Imports argv from module sys to take modules
from sys import argv

# Sets filename to first module
script, filename = argv

# Opens the target file "filename"
txt = open(filename)

print(f"Here's your file {filename}:")
# Prints the output of reading the file
print(txt.read())

# Closes the text file when done
txt.close()

# The process is repeated, this time using "input" instead of "argv" module
print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())

txt_again.close()


# line 1-3 gets the filename

# sets txt to opening the filename. thus txt.read() is a function that reads
# the file without needing to define file parameter.

# txt is (strictly) a 'file object'
# the "." gives the file a command.

# "commands" = "functions" = "methods"

# If I get rid of lines 5-10 (originally) then it would only follow my input
# and ignore the argument variable

# txt = open(filename) actually makes something called a ”file object.”
# similar to a mounted drive
