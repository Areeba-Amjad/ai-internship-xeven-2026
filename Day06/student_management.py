students = ["Ali", "Ahmed", "Sara", "Hina", "Usman"]

print("Initial Student List:", students)
students.append("Ayesha")

print("After append():", students)
students.insert(1, "Fatima")

print("After insert():", students)
students.remove("Ahmed")

print("After remove():", students)
removed_student = students.pop()

print("Removed student using pop():", removed_student)
print("After pop():", students)
first_three = students[:3]

print("First 3 Students:", first_three)
students.sort()

print("Sorted Student List:", students)