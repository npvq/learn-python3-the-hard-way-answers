print("Mary had a little lamb")
print("Its fleece was white as {}.".format('snow'))  # formatted "snow" outside
print("And everywhere that Mary went.")
print("." * 10)  # what'd that do?

end1 = "C"  # Defines the individual characters
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# watch that comma at the end.  try removing it to see what happens
# Result: Syntax Error: invalid syntax.
print(end1 + end2 + end3 + end4 + end5 + end6, end=' ')
print(end7 + end8 + end9 + end10 + end11 + end12)

# When the "end = ''" is removed from line 20,
# The line break is set to the default \n and the next string starts on the
# next line.
