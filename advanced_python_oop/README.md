# Advanced Python Classes and Objects

## Project Overview
This project provides practice exercises to deepen your understanding of Python's Object-Oriented Programming (OOP) concepts, including constructors, destructors, magic methods, inheritance, and composition. The exercises focus on creating classes with specific behaviors and testing them to ensure proper functionality.

## Learning Objectives
- Understand and implement constructors (`__init__`) and destructors (`__del__`) in Python classes.
- Use magic methods (`__str__` and `__repr__`) to define custom string representations for objects.
- Apply inheritance to create class hierarchies and extend functionality.
- Demonstrate proficiency in creating and testing Python classes.

## Directory Structure
```
advanced_python_oop/
├── README.md
├── exercise1_person.py
├── exercise2_book.py
└── exercise3_animal_dog.py
```

## Exercises
1. **Exercise 1: Constructors and Destructors**
   - **File**: `exercise1_person.py`
   - **Description**: Create a Person class with attributes like name and age. Implement a constructor (__init__) to initialize these attributes. Also, implement a destructor (__del__) method to print a farewell message when an object is deleted

2. **Exercise 2: Magic Methods (str and repr)**
   - **File**: `exercise2_book.py`
   - **Description**: Create a Book class with attributes like title, author, and pages. Implement both __str__ and __repr__ magic methods to provide different string representations of the book object.

3. **Exercise 3: Class Inheritance**
   - **File**: `exercise3_animal_dog.py`
   - **Description**: Create a base class Animal with methods like eat and sleep. Create a subclass Dog that inherits from Animal and adds a method bark. Create instances of both classes and demonstrate method inheritance.

## Expected Output:
- **Exercise 1:**
```
Created Person: Alice, 30 years old
Person details: Alice, 30
Farewell, Alice!
```


- **Exercise 2:**
```
Python 101 by Johny Boy, 200 pages
Book(title='Python 101', author='Johny Boy', pages=200)
```


- **Exercise 3:**
```
Generic is eating.
Generic is sleeping.
Buddy is eating.
Buddy is sleeping.
Buddy says Woof!
```


## Notes
- The destructor in Exercise 1 (`__del__`) may not always execute immediately due to Python's non-deterministic garbage collection. For critical resource management, consider using context managers or the `with` statement.
