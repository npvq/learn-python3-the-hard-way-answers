formatter = "{} {} {} {}"  # Sets a variable with four {} brackets

print(formatter.format(1, 2, 3, 4))
# Calls the format function to fill with integers 1, 2, 3, 4
print(formatter.format("one", "two", "three", "four"))
# Calls the format function to fill with strings
print(formatter.format(True, False, True, False))
# Calls the format function to fill with booleans
print(formatter.format(formatter, formatter, formatter, formatter))
# Calls the format function to will formatter with itself, can be used
# recursively.
print(formatter.format(
      "Try your",
      "Own text here",
      "Maybe a poem",
      "Or a song about fear",
      ))
# Calls the formatter function to fill with text over multiple lines, new lines
# and closing bracket should be indented appropriately.
