# Inheritance and Polymorphism

## Project Overview
This project provides practice exercises to master inheritance and polymorphism in Python's Object-Oriented Programming (OOP). The exercises focus on implementing single and multiple inheritance, method overriding, and polymorphic behavior using duck typing. Each exercise demonstrates how to create class hierarchies and leverage polymorphism for flexible and reusable code.

## Learning Objectives
- Understand and implement single, multiple, and multilevel inheritance in Python classes.
- Explain and apply Method Resolution Order (MRO) in multiple inheritance scenarios.
- Utilize method overriding to achieve polymorphism.
- Implement duck typing to enable polymorphic behavior without explicit inheritance.
- Create and test Python classes to demonstrate inheritance and polymorphism.

## Directory Structure
```
inheritance_polymorphism/
├── README.md
├── exercise1_shape_rectangle.py
├── exercise2_bird_mammal_bat.py
└── exercise3_polymorphism_duck_typing.py
```

## Exercises
1. **Exercise 1: Single Inheritance**
   - **File**: `exercise1_shape_rectangle.py`
   - **Description**: Create a base class Shape with a method calculate_area(). Create a subclass Rectangle that inherits from Shape and overrides calculate_area() to calculate the area of a rectangle.


2. **Exercise 2: Multiple Inheritance**
   - **File**: `exercise2_bird_mammal_bat.py`
   - **Description**: Create two parent classes Bird and Mammal with methods fly() and run(), respectively. Create a subclass Bat that inherits from both Bird and Mammal and implements fly() and run() methods


3. **Exercise 3: Polymorphism with Duck Typing**
   - **File**: `exercise3_polymorphism_duck_typing.py`
   - **Description**: Create classes Dog, Cat, and Bird, each with a method make_sound(). Implement different behaviors for make_sound() in each class. Create a function let_them_speak() that takes a list of objects and calls their make_sound() method polymorphically.

## Expected Output
- **Exercise 1:**
```
Base shape area calculation not implemented.
Area of Rectangle: 15
```

- **Exercise 2**
```
Bat is flying.
Bat is running.
```

- **Exercise 3**
```
Dog says Woof!
Cat says Meow!
Bird says Tweet!
```


## Notes
- For Exercise 2, the Method Resolution Order (MRO) can be checked using `Bat.__mro__` to understand how Python resolves method calls in multiple inheritance.
- Exercise 3 demonstrates duck typing, where the `let_them_speak` function works with any object that has a `make_sound` method, regardless of its class.
