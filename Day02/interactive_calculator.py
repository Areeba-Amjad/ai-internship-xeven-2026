"""
Interactive Calculator

This script asks the user for two numbers and calculates their
sum, difference, product, and quotient. It also handles invalid
inputs and division by zero.
"""

try:
    # Ask the user for the first number.
    first_number = float(input("Enter the first number: "))

    # Ask the user for the second number.
    second_number = float(input("Enter the second number: "))

    # Calculate the sum.
    sum_result = first_number + second_number

    # Calculate the difference.
    difference_result = first_number - second_number

    # Calculate the product.
    product_result = first_number * second_number

    # Calculate the quotient.
    if second_number == 0:
        quotient_result = "Cannot divide by zero"
    else:
        quotient_result = first_number / second_number

    # Display the calculator results.
    print("\n===== Calculator Results =====")
    print(
        f"The sum of {first_number:g} and {second_number:g} is: "
        f"{sum_result:g}"
    )
    print(
        f"The difference of {first_number:g} and {second_number:g} is: "
        f"{difference_result:g}"
    )
    print(
        f"The product of {first_number:g} and {second_number:g} is: "
        f"{product_result:g}"
    )
    print(
        f"The quotient of {first_number:g} and {second_number:g} is: "
        f"{quotient_result}"
    )

except ValueError:
    # Handle non-numeric input.
    print("Error: Please enter valid numbers.")