i = 0
numbers = []


def loop(i, increment, end):
    print(f"At the top i is {i}")
    numbers.append(i)

    i += increment
    print("Numbers now: ", numbers)
    print(f"At the bottom i is {i}")

    if i < end:
        # The loop passes its variables onto itself again
        # Note that this won't happen if the "end" number has been reached
        loop(i, increment, end)
        # The number "end" will not be appended to the list "numbers"
        # Because it is above the incrementation of i.


# Calling the loop() Function
loop(i, 1, 6)

print("The numbers: ")

for num in numbers:
    print(num)


# Study Drill 5: Converted ex31.1.py to use for loops and range

# Recall: "range(start, stop[, step])" -pydoc
# –> Range takes an optional step/increment integer value;
# therefore an "increment" variable is not necesary.
