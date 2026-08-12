# Create two parallel lists for student names and grades
student_names = ["Ali", "Ahmed", "Sara", "Hina", "Usman"]
student_grades = [85, 72, 91, 45, 68]

# Find the highest grade and its index
highest_grade = max(student_grades)
highest_index = student_grades.index(highest_grade)
highest_student = student_names[highest_index]

# Find the lowest grade and its index
lowest_grade = min(student_grades)
lowest_index = student_grades.index(lowest_grade)
lowest_student = student_names[lowest_index]

# Calculate the average grade
average_grade = sum(student_grades) / len(student_grades)

# Find students who passed
passed_students = []

for index in range(len(student_names)):
    if student_grades[index] >= 50:
        passed_students.append(student_names[index])

# Display the results
print("===== Grade Tracker =====")
print("Highest Grade:", highest_grade)
print("Highest Grade Student:", highest_student)

print("Lowest Grade:", lowest_grade)
print("Lowest Grade Student:", lowest_student)

print("Average Grade:", average_grade)

print("Passed Students:", passed_students)