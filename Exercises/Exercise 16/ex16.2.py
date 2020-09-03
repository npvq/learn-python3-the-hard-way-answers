# Simplified Version of ex16.0.py
from sys import argv

script, filename = argv  # <--ex16_test.txt

print(f"We're going to erase {filename}.")

# Reads out the current contents of the file
read_target = open(filename, 'r')
print(f"It currently contains the following content:\n\n{read_target.read()}")
read_target.close()

print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

input("?")

print("Opening and truncating the file... (Goodbye!)")
target = open(filename, 'w')

print("Now I'm going to ask you for three lines.")

# This is a sophisticated way to avoid setting the three lines as variables
for i in range(3):
    target.write(str(input(f"line {str(i + 1)}: ") + '\n'))
    # The input command will display its corresponding line number as if
    # we wrote it manually, and return that value to be appended to the file.

print(f"I have written the lines into the file {filename}\nAnd finally, we "
      "close it.")
target.close()


# Key changes:
# deleted "truncate"
# inserts strings to file while typing (at the current stage it shouldn't cause
# problems).
# added a "read" function before truncating file.
