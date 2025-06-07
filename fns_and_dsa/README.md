# Functions, Data Structures, and Modules Project

## Overview
This project, focuses on mastering the fundamentals of **functions**, **data structures**, and **modules** in Python. It includes four tasks that explore defining and using functions, managing data with built-in data structures (e.g., lists), and leveraging Python’s standard and external modules.

## Objectives
- Define the purpose and importance of functions in Python programming.
- Construct functions using def and lambda keywords, understanding proper syntax.
- Work with function parameters, argument passing mechanisms, default values, and keyword arguments.
- Explain the concept of return values and utilize the return statement effectively.
- Distinguish between local and global variable scope within functions.
- Apply global and nonlocal keywords appropriately to manage variable scope.
- Identify common Python data structures: Lists, Tuples, Sets, and Dictionaries.
- Select the appropriate data structure based on the type of data and operations needed.
- Perform operations on Lists (indexing, slicing, appending, etc.).
- Utilize Dictionary methods, understand the immutability of Tuples, and perform Set operations.
- Explain the concepts of modules and packages in Python.
- Create and use custom modules, and import standard modules provided by Python.
- Install and use external Python libraries using pip.
- Identify some essential Python libraries and their functionalities (e.g., requests).
- Comprehend the LEGB rule (Local, Enclosing, Global, Built-in) for understanding variable scope in Python.
- Implement best practices for effective variable scope management.
- Explain the concept of namespaces in Python and differentiate between their types.
- Describe the lifecycle of a namespace and how scope resolution works in Python.

This project equips you with the building blocks for creating well-organized and efficient Python programs. By mastering these concepts, you’ll be able to write clean, maintainable, and reusable code.

## Repository
- **GitHub Repository**: [alx_be_python](https://github.com/BunnyeNyash/alx_be_python.git)
- **Directory**: `fns_and_dsa`

## Directory Structure
```
fns_and_dsa/
├── README.md
├── arithmetic_operations.py
├── shopping_list_manager.py
├── explore_datetime.py
├── temp_conversion_tool.py
└── main.py
```

## Task Descriptions

### Task 0: Arithmetic Operations Function (`arithmetic_operations.py`)
- **Objective**: Create a function to perform basic arithmetic operations (add, subtract, multiply, divide).
- **Description**: Define a `perform_operation` function that takes two floats (`num1`, `num2`) and an operation string (`add`, `subtract`, `multiply`, `divide`). The function returns the result of the operation, handling division by zero gracefully. The provided `main.py` imports and tests this function.
- **Requirements**:
  - Handle four operations with proper logic.
  - Return a specific message or value for division by zero.
    
- **Example Output** (using `main.py`):
  ```
  Arithmetic Operations
  Enter the first number: 5
  Enter the second number: 6
  Enter the operation (add, subtract, multiply, divide): add
  Result: 11.0
  ```
- **File**: `arithmetic_operations.py`

### Task 1: Shopping List Manager (`shopping_list_manager.py`)
- **Objective**: Use Python lists to create a shopping list manager.
- **Description**: Implement a script with a menu-driven interface to add, remove, and view items in a `shopping_list`. The script uses a loop to display options until the user exits, handling invalid inputs and item-not-found cases.
- **Requirements**:
  - Start with an empty `shopping_list`.
  - Provide options to add, remove, view items, and exit.
  - Handle invalid menu choices and missing items gracefully.
    
- **Example Output**:
  ```
  Shopping List Manager
  1. Add Item
  2. Remove Item
  3. View List
  4. Exit
  Enter your choice: 1
  Enter item to add: Apples
  Apples added to the list!
  ```
- **File**: `shopping_list_manager.py`

### Task 2: Explore `datetime` Module (`explore_datetime.py`)
- **Objective**: Use the `datetime` module to work with dates and times.
- **Description**: Create a script with two functions:
  - `display_current_datetime`: Prints the current date and time in “YYYY-MM-DD HH:MM:SS” format, storing the date in `current_date`.
  - `calculate_future_date`: Prompts for a number of days, calculates the future date, and prints it in “YYYY-MM-DD” format, storing it in `future_date`.
- **Requirements**:
  - Use `datetime.now()` and `timedelta` for date calculations.
  - Format outputs as specified.
    
- **Example Output**:
  ```
  Current date and time: 2025-06-07 15:30:45
  Enter the number of days to add to the current date: 10
  Future date: 2025-06-17
  ```
- **File**: `explore_datetime.py`

### Task 3: Temperature Conversion Tool (`temp_conversion_tool.py`)
- **Objective**: Demonstrate variable scope using global variables for temperature conversion.
- **Description**: Create a script with global variables `FAHRENHEIT_TO_CELSIUS_FACTOR` and `CELSIUS_TO_FAHRENHEIT_FACTOR`. Implement `convert_to_celsius` and `convert_to_fahrenheit` functions to convert temperatures, and prompt the user for input, validating temperature and unit inputs.
- **Requirements**:
  - Use global conversion factors.
  - Validate user input, raising an error for non-numeric temperatures.
  - Handle Celsius or Fahrenheit input correctly.
    
- **Example Output**:
  ```
  Enter the temperature to convert: 100
  Is this temperature in Celsius or Fahrenheit? (C/F): F
  100.0°F is 37.77777777777778°C
  ```

  OR
  ```
  Enter the temperature to convert: 0
  Is this temperature in Celsius or Fahrenheit? (C/F): C
  0.0°C is 32.0°F
  ```
- **File**: `temp_conversion_tool.py`

## Prerequisites
- Python 3.x .
- A text editor or IDE.
- For Task 2, familiarity with the `datetime` module (part of Python’s standard library).
- For external libraries, `pip` for installing packages.

## Notes
- Each script is standalone and can be run independently, except for `arithmetic_operations.py`, which requires the provided `main.py` for testing.
- Refer to Python’s official documentation for details on the `datetime` module or other standard libraries.
- The project emphasizes practical application of functions, data structures, modules, and variable scope, aligning with the LEGB rule and namespace concepts.
