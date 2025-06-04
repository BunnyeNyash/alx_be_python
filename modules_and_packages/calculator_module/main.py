"""
Exercise 1: Creating and Using Modules

Instructions:

Create a custom Python module named calculator.py that contains functions for basic arithmetic operations (addition, subtraction, multiplication, division).
Create functions add, subtract, multiply, and divide in the calculator.py module.
Import the calculator module into a separate Python script main.py and use its functions to perform arithmetic operations on numbers like 5 and 3.
"""

# Import the calculator module
import calculator

# Basic arithmetic operations
num1 = 5
num2 = 3

# Addition
print(f"Addition of {num1} and {num2}: {calculator.add(num1, num2)}")            # Output: Addition of 5 and 3: 8

# Subtraction
print(f"Subtraction of {num1} and {num2}: {calculator.subtract(num1, num2)}")    # Output: Subtraction of 5 and 3: 2

# Multiplication
print(f"Multiplication of {num1} and {num2}: {calculator.multiply(num1, num2)}")  # Output: Multiplication of 5 and 3: 15

# Division
try:
    print(f"Division of {num1} by {num2}: {calculator.divide(num1, num2)}")        # Output: Division of 5 by 3: 1.6666666666666667
except ValueError as e:
    print(f"Error: {e}")
