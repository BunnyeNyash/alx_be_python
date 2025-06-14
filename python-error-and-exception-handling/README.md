# Python Exception Handling Practice Exercises

## Overview

This repository contains practice exercises designed to help master errors and exception handling in Python. These exercises cover handling built-in exceptions, raising exceptions, and creating custom exceptions.

## Learning Objectives
- Differentiate between syntax errors and exceptions.
- Identify common Python exceptions and their causes.
- Utilize try, except,else, and finally blocks for exception handling.
- Raise exceptions with raise and create custom exceptions.
- Write code that anticipates and gracefully handles potential errors.


## Practice Exercises
### Exercise 1: Handling ZeroDivisionError

**Instructions:**

- Write a program that takes two numbers as input from the user and divides the first number by the second number.
- Handle the ZeroDivisionError exception to inform the user if they attempt to divide by zero.

**Example Output**
```
Enter the first number: 10
Enter the second number: 2
Result: 5.0
Calculation attempt completed.

Enter the first number: 10
Enter the second number: 0
Error: Cannot divide by zero!
Calculation attempt completed.

Enter the first number: abc
Enter the second number: 2
Error: Please enter valid numbers!
Calculation attempt completed.
```

### Exercise 2: File Handling with FileNotFoundError

**Instructions:**

- Write a program that attempts to open and read data from a file specified by the user.
- Handle the FileNotFoundError exception to provide a meaningful message if the file does not exist.

**Example Output**
```
Enter the file name: data.txt
File contents:
This is a sample text file for testing file handling in Python.
It contains multiple lines of text.
You can use this file to verify that your program can read files successfully.
File operation completed.

Enter the file name: missing.txt
Error: The file 'missing.txt' does not exist.
File operation completed.

Enter the file name: restricted.txt
Error: Permission denied to access 'restricted.txt'.
File operation completed.
```

### Exercise 3: Custom Exception

**Instructions:**

- Create a custom exception class called ValueTooHighError that inherits from the Exception class.
- Write a program that takes a number as input and raises a ValueTooHighError exception if the number is greater than 100.

**Example Output**
```
Enter a number: 50
Success: 50 is valid.
Input validation completed.

Enter a number: 150
Error: 150 is too high. Must be 100 or less.
Input validation completed.

Enter a number: abc
Error: Please enter a valid number!
Input validation completed.
```

## Directory Structure
```
python-error-and-exception-handling/
├── README.md                   # This file
├── zero_division.py            # ZeroDivisionError exercise
├── file_handling.py            # FileNotFoundError exercise
├── custom_exception.py         # Custom exception exercise
└── data.txt                    # samaple file for exercise 2
```
