# Operand "//" = Quotient without Remainder

name = 'Zed A. Shaw'
age = 35  # not a lie
height = 74.0  # inches (in floating point for conversion)
height_int = int(height)  # to keep the printed strings as integers
weight = 180.0  # lbs (in floating point for conversion)
weight_int = int(weight)  # to keep the printed strings as integers
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'
print(f"Let\'s talk about {name}.")
print(f"He\'s {height} inches tall.")
print(f"He\'s {weight} pounds heavy.")
print("Actually that\'s not too heavy.")
print(f"He\'s got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# This line is tricky, try to get it exactly right
total = age + height_int + weight_int
print(f"If I add {age}, {height_int}, and {weight_int} I get {total}.")

# Conversions
height_in_cm = height * 2.54
print(f"He is also {int(round(height_in_cm // 100))} meters and "
      f"{int(round(height_in_cm % 100))} centimeters tall")
weight_in_kg = weight * 0.45
print(f"And, he is approximately {int(round(weight_in_kg))} kilograms heavy")
