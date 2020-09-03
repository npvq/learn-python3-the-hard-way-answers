cars = 100
space_in_a_car = 4.0  # <-Replace with Integer
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
# Cars that are not being driven because there are no available drivers
cars_driven = drivers
# Cars with an available driver to drive them
carpool_capacity = cars_driven * space_in_a_car
# The number of people that they can carry/transport
average_passengers_per_car = passengers / cars_driven
# The average number of passengers that will have to fit in a car (Approximate)

print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to have about", average_passengers_per_car, "in each car.")

# A floating point ensures that decimals will be incoporated rather than being
# rounded to the nearest integer. It is useful when the numbers that we deal
# with are not integers
