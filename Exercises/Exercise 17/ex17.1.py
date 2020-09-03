from sys import argv

script, from_file, to_file = argv

out_file = open(to_file, 'w').write(open(from_file).read())  # <––The Line

# Reference ex17.0.py, the whole copy command was abbreviated to one line.
