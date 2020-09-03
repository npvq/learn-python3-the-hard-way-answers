# Completed Ex23 Challenge

import sys
script, input_encoding, error = sys.argv


def main(language_file, encoding, errors):
    line = language_file.readline()

    if line:
        print_line(line, encoding, errors)
        return main(language_file, encoding, error)


def print_line(line, encoding, errors):
    next_lang = line.strip()
    raw_bytes = next_lang.decode(encoding, errors=errors)
    cooked_string = raw_bytes.encode(encoding, errors=errors)

    print(raw_bytes, "<===>", cooked_string)


languages = open("languages.txt", 'rb')

main(languages, input_encoding, error)
