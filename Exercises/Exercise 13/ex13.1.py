from sys import argv
# read the WYSS (What You Should See) section or ex13.0.py for how to run this
script, first, second, third = argv

fourth = input('Please enter fourth variable: ')
fifth = input('Please enter fifth variable: ')

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)
print("Your fourth variable is:", fourth)
print("Your fifth variable is:", fifth)

# Warning: Scripts like these cannot be ran using IDLE properly,
# they are suited for the command line
