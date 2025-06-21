# More about OOP

## Project Overview

This project dives into advanced Object-Oriented Programming (OOP) concepts in Python. It covers constructors, destructors, magic methods, inheritance, composition, polymorphism, class methods, and static methods. The project includes four mandatory tasks designed to solidify understanding of these concepts through practical implementations. Each task focuses on a specific aspect of OOP, with provided test scripts (main.py) to verify functionality. They're all main.py files but will be renamed here for file naming purposes.

## Repository
**GitHub Repository:** [alx_be_python](https://github.com/BunnyeNyash/alx_be_python.git)

**Directory:** `oop`

**Files:** `book_class.py`, `library_system.py`, `polymorphism_demo.py`, `class_static_methods_demo.py`

## Project Objectives
- Describe the functionalities of constructors (__init__), destructors (__del__), and common magic methods (e.g., __str__, __repr__) in Python classes.
- Implement inheritance to create new classes that inherit properties and methods from existing classes.
- Utilize composition as an alternative to inheritance for building complex objects.
- Explain the concepts of single, multiple, and multilevel inheritance in Python.
- Understand the method resolution order (MRO) in Python and how it affects method calls in inheritance hierarchies.
- Implement polymorphism and method overriding to create flexible and reusable code.
- Explain and use Python’s duck typing to achieve polymorphic behavior.
- Distinguish between class methods and static methods based on their usage and purpose.
- Apply @classmethod and @staticmethod decorators appropriately in your Python classes.

## Directory Structure
```
oop/
├── README.md
├── book_class.py
├── main.py                          # for book_class.py and keeps the main.py name
├── library_system.py
├── main.py                          # for the library_system.py but renamed to main1.py
├── polymorphism_demo.py
├── main.py                          # for the polymorphism_demo.py but renamed to main2.py
├── class_static_methods_demo.py
└── main.py                          # for class_static_methods_demo.py but renamed to main3.py
```


## Tasks
1. **Dive into Python Magic Methods**
   - **File**: `book_class.py`
   - **Description**: Implements a `Book` class with attributes `title`, `author`, and `year`. Includes magic methods `__init__` (constructor), `__del__` (destructor), `__str__` (informal string representation), and `__repr__` (official string representation).
   - **Expected Output** (when running `main.py`):
     
     ```
     1984 by George Orwell, published in 1949
     Book('1984', 'George Orwell', 1949)
     Deleting 1984
     ```
   - **Requirements**:
     - `__init__`: Initializes `title`, `author`, and `year`.
     - `__del__`: Prints "Deleting (title of the book)".
     - `__str__`: Returns "(title) by (author), published in (year)".
     - `__repr__`: Returns `f"Book('{self.title}', '{self.author}', {self.year})"`.

2. **Mastering Inheritance and Composition in Python**
   - **File**: `library_system.py`
   - **Description**: Implements a `Book` base class, derived classes `EBook` and `PrintBook`, and a `Library` class using composition to manage a list of books. `EBook` has an additional `file_size` attribute, and `PrintBook` has a `page_count` attribute.
   - **Expected Output** (when running `main.py`):
     
     ```
     Book: Pride and Prejudice by Jane Austen
     EBook: Snow Crash by Neal Stephenson, File Size: 500KB
     PrintBook: The Catcher in the Rye by J.D. Salinger, Page Count: 234
     ```
   - **Requirements**:
     - `Book`: Base class with `title` and `author`.
     - `EBook` and `PrintBook`: Inherit from `Book`, with unique attributes and proper constructor calls.
     - `Library`: Manages a list of books with `add_book` and `list_books` methods.

3. **Exploring Polymorphism and Method Overriding**
   - **File**: `polymorphism_demo.py`
   - **Description**: Implements a `Shape` base class with an `area` method raising `NotImplementedError`, and derived classes `Rectangle` and `Circle` overriding `area` to calculate their respective areas.
   - **Expected Output** (when running `main.py`):
     
     ```
     The area of the Rectangle is: 50
     The area of the Circle is: 153.93804002589985
     ```
   - **Requirements**:
     - `Shape`: `area` raises `NotImplementedError`.
     - `Rectangle`: Calculates area as `length × width`.
     - `Circle`: Calculates area as `π × radius²` (using `math.pi`).

4. **Distinguishing Between Class Methods and Static Methods**
   - **File**: `class_static_methods_demo.py`
   - **Description**: Implements a `Calculator` class with a static method `add`, a class method `multiply` that references a class attribute `calculation_type`, and prints it before calculating the product.
   - **Expected Output** (when running `main.py`):
     
     ```
     The sum is: 15
     Calculation type: Arithmetic Operations
     The product is: 50
     ```
   - **Requirements**:
     - Class attribute: `calculation_type = "Arithmetic Operations"`.
     - `@staticmethod add(a, b)`: Returns `a + b`.
     - `@classmethod multiply(cls, a, b)`: Prints `calculation_type` and returns `a * b`.
    

## Notes
- The __del__ method in Task 0 may not execute immediately due to Python’s garbage collection; the del statement in main.py triggers it for testing.
- Task 1 demonstrates both inheritance (EBook, PrintBook from Book) and composition (Library managing books).
- Task 2 emphasizes polymorphism through method overriding, with NotImplementedError ensuring subclasses implement area.
- Task 3 highlights the difference between @classmethod (accesses class state) and @staticmethod (independent of class/instance state).
