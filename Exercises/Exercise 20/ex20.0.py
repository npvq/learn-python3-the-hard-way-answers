from sys import argv

script, input_file = argv


def print_all(f):
    print(f.read())


def rewind(f):
    f.seek(0)


def print_a_line(line_count, f):
    print(str(line_count), f.readline())


current_file = open(input_file)

print("First let's print the while file:\n")

print_all(current_file)

print("Now let's rewind, kind of like a tape.")

rewind(current_file)

print("Let's print three lines:")

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)


# Warning: Scripts like these cannot be ran using IDLE properly,
# they are suited for the command line

# Usage Example: ex20.0.py ex20_sample.txt
