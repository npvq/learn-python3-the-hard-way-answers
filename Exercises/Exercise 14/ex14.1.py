from sys import argv

script, user_name, password = argv
prompt = 'Say Something: I\'m Saying...'

print(f"Hi, {user_name}, I'm the {script} script.")
print(f"Your entered {password} as your password")
print('''now we need to verify your credentials
please answer the following authentication questions:
''')
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
Your account has been verified.
""")

# Some creativity to fulfill the Study Drills' requirements

# Warning: Scripts like these cannot be ran using IDLE properly,
# they are suited for the command line
