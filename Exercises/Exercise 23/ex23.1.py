# Simple script argv setup
import sys
script, input_encoding, error = sys.argv


# Main part of function (called at the end)
def main(language_file, encoding, errors):
    # Reads 1 line from the languages file it is given
    line = language_file.readline()

    # Evaluates if readline returned a non-empty strings
    # readline will return an empty string at the end of the file
    if line:
        # Simplifies code by calling another function
        print_line(line, encoding, errors)
        # Repeats the main function, and breaks when the if statement is no
        # longer satisfied, or when readline is at EOF of the languages file.
        return main(language_file, encoding, error)


# This function does the encoding and printing of results (the acutal stuff)
def print_line(line, encoding, errors):
    # Removes/Strips the training \n at the end of the line
    next_lang = line.strip()
    # Encodes (DBES) string next_lang
    raw_bytes = next_lang.encode(encoding, errors=errors)
    # Decodes (DBES) bytes raw_byte, which should be same as next_lang
    cooked_string = raw_bytes.decode(encoding, errors=errors)

    # Prints both of them out
    print(raw_bytes, "<===>", cooked_string)


# After function definitions are finished, open the languages.txt file
languages = open("languages.txt", encoding="utf-8")

# Runs the main "loop"
main(languages, input_encoding, error)


# Unicode is a 4-byte (16-bit) long codec for storing all languages' letters
# and other symbols.
# UTF-8 (Unicode Transformation Format 8 Bits) allows us to store the common
# Roman letters in the compact 8 bits and "escape" into Unicode when there
# are special characters outside of the ASCII 8-bit codec.

# Unicode codec and binary in Python:
# >>> 0b1011010 -> 90 (binary to integer)
# >>> ord('Z') -> 90 (symbol/letter to corresponding codec integer)
# >>> chr(90) -> 'Z' (integer to corresponding codec symbol/letter)
# specify raw Python Numerical/hexadecimal Bytes using b'' (b'\xxx\xxx')

# Mnemonic "DBES" : "Decode Bytes, Encode Strings."
# x.encode -> Encodes/"cooks" strings/characters back to raw bytes
# x.decode -> Decodes raw unicode bytes back to characters/strings

# Refer to document ex23_pyoutput.txt
# Everything on the left of <===> are (raw) Python Numerical Bytes
# They are displayed in hexadecimal, and they are how Python stores the string
# Everything on the right of <===> are "cooked" so you could see the characters
