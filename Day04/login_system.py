# Advanced Login System
# Day 4 - Operators & Type Conversion


# Get user information
username = input("Enter your username: ")
password = input("Enter your password: ")
age_input = input("Enter your age: ")

# Convert age from string to integer
age = int(age_input)

# Validate username
if len(username) < 5:
    print("Error: Username must be at least 5 characters long.")

# Validate password
if len(password) < 8:
    print("Error: Password must be at least 8 characters long.")

# Validate age
if age < 18:
    print("Error: You must be 18 or above to access the system.")

# Check all login conditions
if (
    len(username) >= 5
    and len(password) >= 8
    and age >= 18
):
    print("Access granted! Login successful.")
else:
    print("Access denied. Please fix the above errors.")
    