from sys import argv  # <–– need to import argv before using it

print("How old are you?", end=' ')
age = input()
print("How tall are you?", end=' ')
# Missing height variable definition:
height = input()
print("How much do you weigh?", end=' ')  # <–– close the bracket
weight = input()

print(f"So, you're {age} old, {height} tall and {weight} heavy.")

script, filename = argv

txt = open(filename)  # <–– 'filenme' typo

print(f"Here's your file {filename}:")  # <–– missing 'f' in 'print("Here'
print(txt.read())  # <–– 'tx.read()' typo

print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())  # <–– 'txt_again_read()' typo


print('Let\'s practice everything.')  # <–– 'Let's' did not escape
print('You\'d need to know \'bout escapes \
      with \\ that do \n newlines and \t tabs.')
# Add '\' before newline to escape.

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print("--------------")  # <–– '---)' missing "
print(poem)
print("--------------")  # <–– 'print(–––' missing "


five = 10 - 2 + 3 - 6  # <–– missing number '6'
print(f"This should be five: {five}")  # <–– close the bracket


def secret_formula(started):  # <–– add the colon
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100  # <–– missing operand 'jars  100'
    return jelly_beans, jars, crates


start_point = 10000
beans, jars, crates = secret_formula(start_point)
# Missing variable 'crates'

# remember that this is another way to format a string
print("With a starting point of: {}".format(start_point))
# it's just like with an f"" string
print(f"We'd have {beans} beans, {jars} jars, and {crates} crates.")

start_point /= 10  # Bonus compact operand syntax

print("We can also do that this way:")
formula = secret_formula(start_point)  # <–– 'startpoint' typo
# this is an easy way to apply a list to a format string
print("We'd have {} beans, {} jars, and {} crates.".format(*formula))


people = 20
cats = 30  # <–– mispelled "cats" as "cates", typo
dogs = 15


if people < cats:
    print("Too many cats! The world is doomed!")
    # Missing brackets around 'print()'


if people > cats:  # <–– 'people < cats' typo
    print("Not many cats! The world is saved!")


if people < dogs:
    print("The world is drooled on!")


if people > dogs:  # <–– fixed missing colon ':'
    print("The world is dry!")


dogs += 5

if people >= dogs:
    print("People are greater than or equal to dogs.")


if people <= dogs:  # <–– fixed missing colon ':'
    print("People are less than or equal to dogs.")  # <–– 'dogs.)' missing "


if people == dogs:  # <–– not '=', typo
    print("There are as many people as dogs.")
    # NOT "People are dogs"
