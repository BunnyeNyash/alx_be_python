# match_case_calculator.py
# This script implements a simple calculator using Match Case statements to handle multiple operations.
# The calculator will prompt the user to enter two numbers and select an operation
# (addition, subtraction, multiplication, or division).
# The script will then perform the selected operation using a Match Case statement and display the result.
# Objective: Learn to use Match Case statements for handling multiple operations in a simple calculator program.

# Prompt for User Input
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operation = input("Choose the operation (+, -, *, /): ").strip()

# Perform the Calculation Using Match Case:
match operation:
    case "+":
        addition = num1 + num2
        # Output the Result
        print(f"The result is {addition}.")

    case "-":
        subtraction = num1 - num2
        # Output the Result
        print(f"The result is {subtraction}.")

    case "*":
        multiplication = num1 * num2
        # Output the Result
        print(f"The result is {multiplication}.")

    case "/":
        if num2 == 0:
            print("Cannot divide by zero.")
        else:
            division = num1 / num2
            # Output the Result
            print(f"The result is {division}.")

    case _:
        print("Invalid Operation selected. Try again!!")
