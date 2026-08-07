# Day 3 - Task 1: Enhanced Age Verification System

# Get the user's name
name = input("Enter your name: ")

# Get the user's age and handle non-numeric input
try:
    age = int(input("Enter your age: "))

    # Check if the age is negative
    if age < 0:
        print("Invalid age! Age cannot be negative.")

    # Classify the person as a child
    elif age < 13:
        print(f"Hello {name}! As a child, you have many things to learn and explore.")

    # Classify the person as a teenager
    elif age <= 17:
        print(f"Hello {name}! As a teenager, you have many opportunities ahead.")

    # Classify the person as an adult
    elif age <= 64:
        print(f"Hello {name}! As an adult, you have many opportunities and responsibilities.")

    # Classify the person as a senior
    else:
        print(f"Hello {name}! As a senior, you have a wealth of experience and wisdom.")

# Handle non-numeric input
except ValueError:
    print("Invalid input! Please enter a valid numeric age.")