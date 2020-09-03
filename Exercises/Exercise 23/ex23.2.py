# Simple script argv setup
import sys
script, input_encoding, error = sys.argv

# This is part of the extreme challenge ex23. I later realized that this script
# Was basically useless, but I am keeping it for documentation sake.


def create_binary(language_file, destination_file, encoding, errors):
    # Reads 1 line from the languages file it is given
    line = language_file.readline()

    # Creates destination binary file:

    # Evaluates if readline returned a non-empty strings
    # readline will return an empty string at the end of the file
    if line:
        # Simplifies code by calling another function
        destination_file.write(make_raw(line, encoding, errors))
        # Repeats the main function, and breaks when the if statement is no
        # longer satisfied, or when readline is at EOF of the languages file.
        return create_binary(language_file, destination_file, encoding, error)


# This Function will help us generate a binary file for the challenge
def make_raw(line, encoding, errors):
    # Removes/Strips the training \n at the end of the line
    next_lang = line.strip()
    # Encodes (DBES) string next_lang
    raw_bytes = next_lang.encode(encoding, errors=errors)
    # Returns raw bytes
    return raw_bytes


# After function definitions are finished, open the languages.txt file
languages = open("languages.txt", 'r', encoding="utf-8")


file = open("ex23_binary.bin", 'wb')


# Runs the main "loop"
create_binary(languages, file, input_encoding, error)
