# simple_interest.py
# Objective: Apply basic Python arithmetic operations and variable assignments to calculate the simple interest on a given principal amount, rate of interest, and time.
"""A Python script that calculates the simple interest earned on an investment over a period of time. The formula for simple interest is (I = P * R * T), where:

( I ) is the interest earned,
( P ) is the principal amount (initial investment),
( R ) is the annual interest rate (as a decimal),
( T ) is the time the money is invested for in years.
"""

# Define the principal amount, rate of interest, and time
principal = 1000  # Principal amount in dollars
rate_of_interest = 0.05  # Annual interest rate (5%)
time = 3  # Time in years

# Calculate the simple interest
interest = principal * rate_of_interest * time

# Print the result
print(f"The simple interest is: {interest}")