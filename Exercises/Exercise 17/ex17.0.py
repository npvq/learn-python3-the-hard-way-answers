from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}.")

# we could do these two on one line, here's how:
# indata = open(from_file).read
in_file = open(from_file)
indata = in_file.read()

print(f"The input file is {len(indata)} bytes long.")

print(f"Does the output file exist? {exists(to_file)}")
print("Ready, his RETURN to continue, CTRL-C to abort.")
input()

out_file = open(to_file, 'w')
out_file.write(indata)

print("Alright, all done.")

out_file.close()
in_file.close()

# Make a test file in bash via: echo "x" > x.txt
# You must close a file when you're done with it because python may not
# automatically close the file when there are unexpected scopes/exits.
# Otherwise, Python does try to automatically close files when the number of
# references to that file decreases to 0.

# Usage Example: python3 ex17.0.py from_file.txt to_file.txt
