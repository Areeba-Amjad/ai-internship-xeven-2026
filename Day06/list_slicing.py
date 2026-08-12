# Create a list of numbers from 1 to 20
numbers = list(range(1, 21))

print("Original List:", numbers)

# Get the first 5 elements
first_five = numbers[:5]
print("First 5 Elements:", first_five)

# Get the last 5 elements
last_five = numbers[-5:]
print("Last 5 Elements:", last_five)

# Get every 3rd element
every_third = numbers[::3]
print("Every 3rd Element:", every_third)

# Reverse the entire list using slicing
reversed_list = numbers[::-1]
print("Reversed List:", reversed_list)

# Get the middle 10 elements
middle_ten = numbers[5:15]
print("Middle 10 Elements:", middle_ten)