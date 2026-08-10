# Task 2: Multi-Operation Calculator

# Get two numbers from the user
number_1 = float(input("Enter first number: "))
number_2 = float(input("Enter second number: "))

# Get the operation from the user
operation = input("Enter operation (+, -, *, /, %, **): ")

# Perform the selected operation
if operation == "+":
    result = number_1 + number_2
    print(f"{number_1:.1f} + {number_2:.1f} = {result:.1f}")

elif operation == "-":
    result = number_1 - number_2
    print(f"{number_1:.1f} - {number_2:.1f} = {result:.1f}")

elif operation == "*":
    result = number_1 * number_2
    print(f"{number_1:.1f} * {number_2:.1f} = {result:.1f}")

elif operation == "/":
    if number_2 == 0:
        print("Error: Division by zero is not allowed.")
    else:
        result = number_1 / number_2
        print(f"{number_1:.1f} / {number_2:.1f} = {result:.1f}")

elif operation == "%":
    if number_2 == 0:
        print("Error: Modulus by zero is not allowed.")
    else:
        result = number_1 % number_2
        print(f"{number_1:.1f} % {number_2:.1f} = {result:.1f}")

elif operation == "**":
    result = number_1 ** number_2
    print(f"{number_1:.1f} ** {number_2:.1f} = {result:.1f}")

else:
    print("Error: Invalid operation. Please choose +, -, *, /, %, or **.")