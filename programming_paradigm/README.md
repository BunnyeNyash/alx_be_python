# Programming Paradigms & Exception Handling

## Overview

This project introduces fundamental concepts of Object-Oriented Programming (OOP) in Python and Exception Handling. It covers classes, objects, encapsulation, abstraction, error handling with try-except blocks, and unit testing using Python's unittest module. The project consists of four tasks designed to build skills in creating robust, maintainable Python applications.

## Objectives
- Explain the core concepts of OOP: classes, objects, encapsulation, and abstraction.
- Discuss the significance of OOP in software development and its advantages over other programming paradigms.
- Define classes and create objects in Python.
- Understand the difference between class attributes, instance methods, and the role of the self keyword within classes.
- Differentiate between syntax errors and exceptions in Python.
- Identify common Python exceptions and understand their causes.
- Utilize try, except, else, and finally blocks to handle exceptions effectively.
- Raise exceptions using the raise keyword and create custom exceptions for specific errors in your code.
- Explain the importance of testing in software development.
- Describe different types of testing, with a focus on unit testing.
- Write basic unit tests using Python’s unittest module to verify the functionality of your code.
- Structure test cases effectively and understand how test runners work.

## Repository
- **GitHub Repository:** [alx_be_python](https://github.com/BunnyeNyash/alx_be_python.git)
- **Directory:** `programming_paradigm`

## Directory Structure
```
programming_paradigm/
├── README.md                                    # This file
├── bank_account.py                              # Implements a BankAccount class for banking operations
├── main-0.py                                    # Tests BankAccount class via command-line arguments
├── robust_division_calculator.py                # Implements a safe_divide function with error handling
├── main.py (for robust_division_calculator)     # Tests safe_divide via command-line arguments
├── simple_calculator.py                         # Provided class with basic arithmetic operations
├── test_simple_calculator.py                    # Contains unit tests for the provided SimpleCalculator class
├── library_management.py                        # Implements Book and Library classes for a library management system
└── main-L.py (for library_management)             # Tests Book and Library classes
```

## Tasks
1. **Create a Simple Bank Account Class**
   - Implements a `BankAccount` class with methods for deposit, withdrawal, and balance display.
   - Tested with `main-0.py` using command-line arguments.
     
   - **Expected Outputs**:
     - Deposit: `python main-0.py deposit:50`
       ```
       Deposited: $50
       ```
     - Withdraw with Sufficient Funds: `python main-0.py withdraw:20`
       ```
       Withdrew: $20
       ```
     - Withdraw with Insufficient Funds: `python main-0.py withdraw:150`
       ```
       Insufficient funds.
       ```
     - Display Balance: `python main-0.py display`
       ```
       Current Balance: $[amount]
       ```

2. **Robust Division Calculator with Command Line Arguments**
   - Implements a `safe_divide` function handling division by zero and non-numeric inputs.
   - Tested with `main.py` using command-line arguments.
     
   - **Expected Outputs**:
     - Normal Division: `python main.py 10 5`
       ```
       The result of the division is 2.0
       ```
     - Division by Zero: `python main.py 10 0`
       ```
       Error: Cannot divide by zero.
       ```
     - Invalid Input (Non-numeric): `python main.py ten 5`
       ```
       Error: Please enter numeric values only.
       ```

3. **Writing Unit Tests for a Simple Calculator Class**
   - Provides unit tests for the provided `SimpleCalculator` class using `unittest`.
   - Tests addition, subtraction, multiplication, and division, including edge cases like division by zero.
     
   - **Expected Output**: Running `python -m unittest test_simple_calculator.py` should produce a test summary indicating all tests pass (e.g., "OK" if all assertions are correct).

4. **Implementing Basic OOP for a Library Management System**
   - Implements `Book` and `Library` classes to manage book checkouts and returns.
   - Tested with `main.py`.
     
   - **Expected Outputs**:
     - After Initial Setup: `python main.py`
       ```
       Available books after setup:
       Brave New World by Aldous Huxley
       1984 by George Orwell
       ```
     - After Checking Out '1984':
       ```
       Available books after checking out '1984':
       Brave New World by Aldous Huxley
       ```
     - After Returning '1984':
       ```
       Available books after returning '1984':
       Brave New World by Aldous Huxley
       1984 by George Orwell
       ```

## Execution
1. Run the main scripts:

- Task 0: **python main-0.py <command>:<amount>** (e.g., python main-0.py deposit:50)
- Task 1: **python main.py <numerator> <denominator>** (e.g., python main.py 10 5)
- Task 3: **python main.py** (for library_management)
  
2. Run tests for Task 2: `python -m unittest test_simple_calculator.py`

## Prerequisites
- **Python:** Version 3.x
- **Tools:** A Code Editor like VS Code, PyCharm or IDLE
