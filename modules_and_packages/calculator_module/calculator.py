"""
Exercise 1: Creating and Using Modules

Instructions: 

Create a custom Python module named calculator.py that contains functions for basic arithmetic operations (addition, subtraction, multiplication, division).
Create functions add, subtract, multiply, and divide in the calculator.py module.
Import the calculator module into a separate Python script main.py and use its functions to perform arithmetic operations on numbers like 5 and 3.
"""

# Addition
def add(num1, num2):
  """Returns the sum of two numbers."""
  return num1 + num2

# Subtraction
def subtract(num1, num2):
  """Returns the difference of two numbers."""
  return num1 - num2

# Multiplication
def multiply(num1, num2):
  """Returns the product of two numbers."""
  return num1 * num2

# Division
def divide(num1, num2):
  """Returns the division of two numbers. Raises an error if dividing by zero."""
  if num2 == 0:
    raise ValueError("Cannot divide by zero")
  return num1 / num2
