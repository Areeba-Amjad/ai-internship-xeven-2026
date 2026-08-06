"""
Data Types Explorer

This script demonstrates basic Python data types, type checking,
and type conversion between different data types.
"""

# Integer variable
age = 21

# Float variable
height = 5.5

# Boolean variable
is_student = True

# String variable
name = "Areeba"

# Display integer value and type
print("===== Python Data Types =====")
print("Integer:", age)
print("Type:", type(age))

# Display float value and type
print("\nFloat:", height)
print("Type:", type(height))

# Display Boolean value and type
print("\nBoolean:", is_student)
print("Type:", type(is_student))

# Display string value and type
print("\nString:", name)
print("Type:", type(name))

# Convert integer to string
age_as_string = str(age)

print("\n===== Type Conversion =====")
print("Integer to String:", age_as_string)
print("Converted type:", type(age_as_string))

# Convert string to float
number_as_string = "25.5"
number_as_float = float(number_as_string)

print("\nString to Float:", number_as_float)
print("Converted type:", type(number_as_float))

# Convert float to integer
price = 99.99
price_as_integer = int(price)

print("\nFloat to Integer:", price_as_integer)
print("Converted type:", type(price_as_integer))
