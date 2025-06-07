# Variable Scope and Namespaces Practice Exercises

## Overview
This repository contains three Python scripts designed to demonstrate the concepts of **variable scope** and **namespaces** in Python. Each script corresponds to a practice exercise that explores how Python manages variables in different scopes (local, enclosing, global, built-in) and namespaces, following the LEGB (Local, Enclosing, Global, Built-in) rule for variable lookup.

## Files
1. **local_vs_global.py**: Demonstrates the difference between local and global scopes using a variable with the same name.
2. **namespace_exploration.py**: Shows how namespaces keep variables with the same name separate in different functions.
3. **scope_hierarchy.py**: Illustrates the LEGB rule with variables defined in global, enclosing, and local scopes, including comments explaining scope resolution.

## Exercise Descriptions

### Exercise 1: Local vs Global Scope (`local_vs_global.py`)
- **Purpose**: Demonstrates how Python distinguishes between variables with the same name in global and local scopes.
- **Description**: Defines a variable `message` in the global scope and inside a function (local scope). Prints the variable inside and outside the function to show how Python accesses the local variable inside the function and the global variable outside.
- **Expected Output**:
  ```
  Inside function: Hello from local scope!
  Outside function: Hello from global scope!
  ```

### Exercise 2: Namespace Exploration (`namespace_exploration.py`)
- **Purpose**: Shows how namespaces prevent conflicts between variables with the same name in different functions.
- **Description**: Defines two functions, each with a local variable named `count` but with different values. Calls both functions to demonstrate that each function’s namespace keeps its `count` variable separate.
- **Expected Output**:
  ```
  Counting function: 5 items processed
  Logging function: 3 events logged
  ```

### Exercise 3: Scope Hierarchy (`scope_hierarchy.py`)
- **Purpose**: Illustrates the LEGB rule for variable lookup across global, enclosing, and local scopes.
- **Description**: Defines a variable `value` in global, enclosing (outer function), and local (inner function) scopes. Prints the variable in each scope and includes comments explaining how Python follows the LEGB rule to resolve variable names.
- **Expected Output**:
  ```
  Inner function (local scope): 10
  Outer function (enclosing scope): 50
  Global scope: 100
  ```

## Learning Objectives
- Understand the difference between local and global scopes.
- Learn how namespaces prevent naming conflicts in Python.
- Explore the LEGB rule for variable lookup in nested scopes.
- Apply best practices for managing variables to write clean, maintainable code.
