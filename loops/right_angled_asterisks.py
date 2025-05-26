# right_angled_asterisks.py
# This script prints a right triangle of asterisks based on user input for the number of rows.

rows = 10

for i in range(1, 11):  # Outer loop for rows
  for j in range(1, i + 1):
    print("*", end="")
  print()  # Move to a new line after each row of asterisks
