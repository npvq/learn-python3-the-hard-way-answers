from sys import argv

script, input_file = argv


def print_all(f):
    # Prints the results from reading the whole file
    print(f.read())


def rewind(f):
    # Changes the seek to 0, at the beginning of the file
    f.seek(0)


def print_a_line(line_count, f):
    # prints line_count and reads line.
    print(line_count, f.readline(), end='')


# opens input_file
current_file = open(input_file)

print("First let's print the while file:\n")

print_all(current_file)

print("Now let's rewind, kind of like a tape.")

rewind(current_file)

print("Let's print three lines:")

# Sets the current line to line 1
current_line = 1
print_a_line(current_line, current_file)

# Increments current line by 1
current_line += 1
print_a_line(current_line, current_file)

# Increments current line by 1
current_line += 1
print_a_line(current_line, current_file)

# += (Increments by x)
# -= (Decrements by x)
# *= (Multiplies by x)
# **= (To the xth power)
# /= (Divides by x)
# //= (Divides by x ignoring remainder)
# %= (Finds mod x of original)


# File.Seek(x) moves the current "reading position" of the file to the xth
# character in the file.
# "Python file method seek() sets the file's current position at the offset."
# -internet
# "seek(offset[, whence]) -> None.  Move to new file position.
#  Argument offset is a byte count.  Optional argument whence defaults to
#  0 (offset from start of file, offset should be >= 0); other values are 1
#  (move relative to current position, positive or negative), and 2 (move
#  relative to end of file, usually negative, although many platforms allow
#  seeking beyond the end of a file).  If the file is opened in text mode,
#  only offsets returned by tell() are legal." -pydoc

# current_line, which is read in the function print_a_line as the variable
# linecount, does not actually affect the printed line in f.readline();
# therefore, this only makes sense if the line_count is consecutively
# incrementing by 1.

# Warning: Scripts like these cannot be ran using IDLE properly,
# they are suited for the command line

# Usage Example: ex20.0.py ex20_sample.txt
