from sys import argv

script, user_name = argv
prompt = '> '

print(f"Hi, {user_name}, I'm the {script} script.")
print("I'd like to ask you a few questions.")
print(f"Do you like me {user_name}?")
likes = input(prompt)

print(f"Where do you live {user_name}?")
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice.
""")

# --Find out what the games Zork and Adventure were. Find a copy and play it.
# they were some of the earliest command line games played using interactions
# between the user and the script via input.

# Warning: Scripts like these cannot be ran using IDLE properly,
# they are suited for the command line
