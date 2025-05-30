# Introducing Logic into Programming (Control Flow and Loops)

## Overview

This project is part of the ALX Backend Python curriculum, focusing on control flow and loops to introduce logic into Python programs. It covers conditional statements (`if`, `elif`, `else`), `match case` statements (Python 3.10+), and loop constructs (`for` and `while`) through practical tasks. The project equips beginners with skills to make decisions, automate repetitive tasks, and create dynamic programs.

## Objectives

- Explain the concept of control flow and its role in programming.
- Utilize conditional statements (if, else, elif) to control the flow of execution in your Python code based on specific conditions.
- Write practical examples demonstrating the use of conditional statements for decision-making.
- Understand the concept of Match Case statements introduced in Python 3.10 as an alternative to multiple if/elif statements (optional for Python versions below 3.10).
- Explain the advantages of Match Case statements for handling multiple conditions.
- Implement Match Case statements using proper syntax, including matching against specific values and types (optional for Python versions below 3.10).
- Apply best practices for using Match Case statements to enhance code readability and efficiency (optional for Python versions below 3.10).
- Grasp the purpose and different types of loops available in Python.
- Utilize for loops to iterate over sequences (lists, tuples, strings, etc.) efficiently.
- Write examples demonstrating how to use for loops to iterate over various data structures.
- Explain the concept of while loops and how they differ from for loops.
- Implement while loops in Python to execute code repeatedly as long as a specific condition remains true.
- Understand nested loops (loops within loops) and their applications in scenarios like working with multidimensional data or creating patterns.

## Repository

- **GitHub Repository**: [alx_be_python](https://github.com/BunnyeNyash/alx_be_python.git)
- **Directory**: `control-flow`

## Directory Structure

```
control-flow/
├── weather_advice.py          # Weather-based clothing recommendations
├── match_case_calculator.py   # Calculator using match case
├── multiplication_table.py    # Multiplication table generator
├── pattern_drawing.py         # Square pattern with nested loops
├── daily_reminder.py          # Task reminder with match case and conditionals
└── README.md                  # Project documentation
```

## File Descriptions

- **weather_advice.py**:
  - Prompts user for weather conditions (`sunny`, `rainy`, `cold`) and provides clothing recommendations using `if`, `elif`, and `else`.
  - Example output:
      ```
      What's the weather like today? (sunny/rainy/cold): sunny
      Wear a t-shirt and sunglasses.
      ```
      OR, for an unexpected input scenario:
    
      ```
      What's the weather like today? (sunny/rainy/cold): windy
      Sorry, I don't have recommendations for this weather.
      ```  

- **match_case_calculator.py**:
  - Takes two numbers and an operation (`+`, `-`, `*`, `/`) as input, performs the calculation using `match case`, and handles division by zero.
  - Example output:
      ```
      Enter the first number: 10
      Enter the second number: 5
      Choose the operation (+, -, *, /): *
      The result is 50.
      ```
      OR, for a division by zero scenario:
    
      ```
      Enter the first number: 10
      Enter the second number: 0
      Choose the operation (+, -, *, /): /
      Cannot divide by zero.
      ```  

- **multiplication_table.py**:
  - Prompts for a number and uses a `for` loop to print its multiplication table (1 to 10).
  - Example output:
      ```
      Enter a number to see its multiplication table: 5
      5 * 1 = 5
      5 * 2 = 10
      5 * 3 = 15
      5 * 4 = 20
      5 * 5 = 25
      5 * 6 = 30
      5 * 7 = 35
      5 * 8 = 40
      5 * 9 = 45
      5 * 10 = 50
      ``` 

- **pattern_drawing.py**:
  - Prompts for a positive integer and uses a `while` loop with a nested `for` loop to print a square pattern of asterisks.
  - Example output:
      ```
      Enter the size of the pattern: 4
      ****
      ****
      ****
      ****
      ``` 

- **daily_reminder.py**:
  - Prompts for a task, priority (`high`, `medium`, `low`), and time sensitivity (`yes`, `no`), using `match case` and `if` statements to generate a customized reminder.
  - Example output:
      ```
      Enter your task: Finish project report
      Priority (high/medium/low): high
      Is it time-bound? (yes/no): yes

      Reminder: 'Finish project report' is a high priority task that requires immediate attention today!
      ```
      OR, for a non-time-bound task:
    
      ```
      Enter your task: Read a book
      Priority (high/medium/low): low
      Is it time-bound? (yes/no): no

      Note: 'Read a book' is a low priority task. Consider completing it when you have free time.
      ```  

## Prerequisites

- **Python**: Version 3.10 or higher (required for `match case` statements)
- **Tools**: A code editor like VS Code, PyCharm, or IDLE and a terminal/command prompt

## Example Interactions

- **weather_advice.py**:
  ```bash
  python3 weather_advice.py
  What's the weather like today? (sunny/rainy/cold): rainy
  Don't forget your umbrella and a raincoat.
  ```

- **match_case_calculator.py**:
  ```bash
  python3 match_case_calculator.py
  Enter the first number: 10
  Enter the second number: 0
  Choose the operation (+, -, *, /): /
  Cannot divide by zero.
  ```

- **multiplication_table.py**:
  ```bash
  python3 multiplication_table.py
  Enter a number to see its multiplication table: 5
  5 * 1 = 5
  5 * 2 = 10
  ...
  5 * 10 = 50
  ```

- **pattern_drawing.py**:
  ```bash
  python3 pattern_drawing.py
  Enter the size of the pattern: 4
  ****
  ****
  ****
  ****
  ```

- **daily_reminder.py**:
  ```bash
  python3 daily_reminder.py
  Enter your task: Read a book
  Priority (high/medium/low): low
  Is it time-bound? (yes/no): no
  
  Note: 'Read a book' is a low priority task. Consider completing it when you have free time.
  ```

## Notes

- Use Python 3.10+ for `match case` suppor
- Refer to Python’s [official documentation](https://docs.python.org/3/) for details on control flow and loops.
