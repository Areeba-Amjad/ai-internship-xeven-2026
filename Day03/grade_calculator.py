# Day 3 - Task 2: Grade Calculator with Feedback

# Get the student's name
name = input("Enter your name: ")

# Get the numeric grade and handle invalid input
try:
    grade = float(input("Enter your grade (0-100): "))

    # Validate that the grade is between 0 and 100
    if grade < 0 or grade > 100:
        print("Invalid grade! Please enter a grade between 0 and 100.")

    # Assign A grade
    elif grade >= 90:
        print(f"Hello {name}!")
        print(f"Your grade is A.")
        print("Excellent work! You have achieved an outstanding result.")

    # Assign B grade
    elif grade >= 80:
        print(f"Hello {name}!")
        print(f"Your grade is B.")
        print("Good job! Keep up the great work.")

    # Assign C grade
    elif grade >= 70:
        print(f"Hello {name}!")
        print(f"Your grade is C.")
        print("Good effort! Keep working to improve.")

    # Assign D grade
    elif grade >= 60:
        print(f"Hello {name}!")
        print(f"Your grade is D.")
        print("You passed, but there is room for improvement.")

    # Assign F grade
    else:
        print(f"Hello {name}!")
        print(f"Your grade is F.")
        print("Keep trying! Review your work and work harder next time.")

# Handle non-numeric input
except ValueError:
    print("Invalid input! Please enter a numeric grade.")