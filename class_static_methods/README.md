# More on Class Methods and Static Methods

## Project Overview
This project provides practice exercises to master class methods and static methods in Python's Object-Oriented Programming (OOP). The exercises focus on using the `@classmethod` and `@staticmethod` decorators to implement methods that operate on class-level data or provide utility functions without requiring instance or class state. Each exercise demonstrates practical applications of these concepts.

## Learning Objectives
- Understand the differences between class methods and static methods in Python.
- Implement class methods using the `@classmethod` decorator to work with class-level data.
- Implement static methods using the `@staticmethod` decorator for utility functions.
- Apply class methods to create factory methods for instantiating objects with specific configurations.
- Test and verify the behavior of class and static methods.

## Directory Structure
```
class_static_methods/
├── README.md
├── exercise1_book.py
├── exercise2_calculator.py
└── exercise3_person.py
```

## Exercises
1. **Exercise 1: Class Methods for Counting Instances**
   - **File**: `exercise1_book.py`
   - **Description**: Create a class Book with a class variable total_books to count the number of book instances created. Implement a class method display_total_books() to display the total number of books created.


2. **Exercise 2: Static Method for Utility Calculation**
   - **File**: `exercise2_calculator.py`
   - **Description**: Create a class Calculator with static methods for basic mathematical operations like addition and multiplication. Implement static methods add() and multiply() to perform these operations.
     

3. **Exercise 3: Class Method for Factory Creation**
   - **File**: `exercise3_person.py`
   - **Description**: Create a class Person with attributes name and age. Implement a class method create_child() to create a new instance representing a child with age set to 0.


## Expected Output
- **Exercise 1:**
```
Total books created: 2
```


- **Exercise 2:**
```
Addition: 8
Multiplication: 15
```


- **Exercise 3:**
```
Person: Alice, Age: 30
Child: Bob, Age: 0
```

## Notes
- Class methods in Exercise 1 and 3 use the `cls` parameter to access class-level data or create instances.
- Static methods in Exercise 2 are independent of class or instance state, making them ideal for utility functions.
