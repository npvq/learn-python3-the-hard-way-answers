from sys import argv
# read the WYSS section for how to run this
script, first, second, third = argv

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)


# How to run it in bash:
# cd (to directory containing ex13.py)
# python3 ex13.py first 2nd 3rd

# When fewer arguements are given, the program does not know what to do with
# the lack of arguements and reports it as an error

# Warning: Scripts like these cannot be ran using IDLE properly,
# they are suited for the command line
