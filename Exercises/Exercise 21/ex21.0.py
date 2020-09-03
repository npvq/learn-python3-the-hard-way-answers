def add(a, b):
    print(f"ADDING {a} + {b}")
    return a + b


def subtract(a, b):
    print(f"SUBTRACTING {a} - {b}")
    return a - b


def multiply(a, b):
    print(f"MULTIPLYING {a} * {b}")
    return a * b


def divide(a, b):
    print(f"DIVIDING {a} / {b}")
    return a / b


print("Let's do some math with just functions!")

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")


# A puzzle for extra credit, type it in anyway.
print("Here is a puzzle.")

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))
# Expression = 25 + 74 - (180 * 50 / 2)

print("That becomes: ", what, "Can you do it by hand?")

# Formula = 24 + 34 / 100 - 1023 (Remember, PEMDAS)
answer = add(24, subtract(divide(34, 100), 1023))
print(f"24 + 34 / 100 - 1023 = {answer}")

# If using user input for functions, use float(input()).
