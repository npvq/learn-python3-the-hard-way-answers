i = 0
numbers = []

# Range(start=1, end, increment)
for i in range(1, 6, 1):
    print(f"At the top i is {i}")
    numbers.append(i)

    print("Numbers now: ", numbers)
    # This is a superficial way of ensuring the same output text
    # as we didn't increment the i value manually – it is iterated
    print(f"At the bottom i is {i + 1}")
    # Again, this continuity only works when increment is set to 1.


print("The numbers: ")

for num in numbers:
    print(num)


# Study Drill 1: Converted while loop to a looping function as demonstrated in
# exercise 23 (ex23.0.py) using "end" as a range max
# Study Drill 3: added a increment factor as "increment"
