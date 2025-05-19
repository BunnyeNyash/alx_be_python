# future_age_calculator.py
# Objective: Practice receiving user input in Python and perform a simple arithmetic operation to calculate the user’s age in a future year.
# A Python script that asks the user for their current age and then calculates how old they will be in a specific future year. This task introduces handling user input and reinforces arithmetic operations.

# Ask the user for their current age
current_age = int(input("How old are you?  "))

# Define the current year and the future year
future_year = 2050
current_year = 2023

# Calculate the user's age in the future year
future_age = current_age + (future_year - current_year)

# Print the result
print(f"In {future_year}, you will be {future_age} years old.")
