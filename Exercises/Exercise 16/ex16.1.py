# Simplified Version of ex16.0.py
from sys import argv

script, filename = argv  # <--ex16_test.txt

print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

input("?")

print("Opening and truncating the file... (Goodbye!)")
target = open(filename, 'w')

print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

# Writes all of the strings and escapes to the file together
target.write(f"{line1}\n{line2}\n{line3}\n")

print(f"I have written the lines into the file {filename}\nAnd finally, we "
      "close it.")
target.close()
