"""
Exercise 3: Write a program to generate a random set of numbers between 1 and ten. Use set operations to remove duplicates and display the unique numbers.
"""

# Import the random library
import random

# Generate a random set of numbers
count = 5
numbers = [random.randint(1, 10) for _ in range(count)]    # List comprehension ... append random.randint(1, 10) ... for statement

# Remove duplicates by converting the list to a set
unique_numbers = set(numbers)

# Display the unique numbers
print("List of numbers with possible duplicates:", numbers)
print("Unique numbers:", unique_numbers)
