the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this first kind of for-loop goes through a list
for number in the_count:
    print(f"this is count {number}")

# same as above
for fruit in fruits:
    print(f"A fruit of type: {fruit}")

# aslo we can go through mixed lists too
# notice we have to use {} since we don't know what's in it
for i in change:
    print(f"I got {i}")

# we can also build lists, first start with an empty one
elements = []

# then use the range function to do 0 to 5 counts
for i in range(0, 6):
    print(f"Adding {i} to the list.")
    # append is a function that lists understand
elements.append(*range(0, 6))

# now we can print them out too
for i in elements:
    print(f"Elements was {i}")

# "range(start, stop[, step]) -> list of integers. start defaults to 0 and
# step is optional." -pydoc
# range(i, j) outputs integers within [i, j) or [i, i+1, i+2 ... j-1].

# We could have skipped the for loop by defining elements as the range directly
# E.g.: elements = [*range(0, 6)]

# Lists Commands:
# x.append(object) append object to end.
# x.count(value) integer -- return number of occurrences of value.
# x.extend(iterable) extend list by appending elements from the iterable.
#       appends multiple iterations/values to the end of the list.
# x.index(value, [start, [stop]]) integer -- return index of
#       the first occurrence of value.
# x.insert(index, object) insert object before index.
# x.pop([index]) remove and return item at index (default last).
#       raises IndexError when given list is empty.
# x.remove(value) remove first occurrence of value.
# x.reverse() reverses the whole list in place.
# x.sort() stable sort in place.
