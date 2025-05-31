# pattern_drawing.py
# This script will prompt the user to enter a positive integer,
# then use nested loops to print a square pattern of that size made of asterisks (*).
# Objective: Utilize while loops and nested for loops to draw a simple text-based pattern.

# Prompt User for Pattern Size:
size = int(input("Enter the size of the pattern: "))

# Draw the pattern
row = 0     # initialize the row count

while row < size:
    for col in range(size):
        print("*", end="")
    print()  # Move to the next line after printing one row
    row += 1
