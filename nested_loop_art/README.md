# Nested Loop Art

## Overview

This project is a Python challenge designed to practice nested `while` loops by creating a text-based pyramid pattern of asterisks (*). The program uses an outer loop to control the number of rows and an inner loop to print spaces and asterisks, forming a triangular shape. This task reinforces understanding of loop control, iteration, and pattern generation in Python.

## Objectives

- Define a variable to set the height of the pyramid (number of rows).
- Use a nested `while` loop structure to control rows and print spaces and asterisks.
- Adjust the number of spaces and asterisks in each row to create a centered pyramid pattern.
- Print the final pyramid pattern, e.g., a 5-row pyramid with increasing asterisks.

## Repository

- **GitHub Repository**: [alx_be_python](https://github.com/BunnyeNyash/alx_be_python.git)
- **Directory**: `nested_loop_art`

## Directory Structure

```
nested_loop_art/
├── pyramid_art.py             # Script to print a pyramid pattern using nested while loops
└── README.md                  # Project documentation
```

## File Descriptions

- **pyramid_art.py**:
  - Defines a variable `rows` (e.g., `rows = 5`) to set the pyramid height.
  - Uses an outer `while` loop to iterate over rows and an inner `while` loop to print spaces followed by asterisks.
  - Adjusts spaces and asterisks based on the row number to form a centered pyramid.
  - Outputs a pyramid pattern, e.g., for `rows = 5`:
```
    *
   ***
  *****
 *******
*********
```
 

## Prerequisites

- **Python**: Version 3.8 or higher
- **Tools**: A code editor like VS Code, PyCharm, or IDLE and a terminal/command prompt


## Example Interaction

```bash
python3 pyramid_art.py
```

**Output** (for `rows = 10`):
```
              *
             ***
            *****
           *******
          *********
         ***********
        *************
       ***************
      *****************
     *******************
```

## Notes

- Test the script with different values of `rows` to confirm the pyramid scales correctly.
- Refer to Python’s [official documentation](https://docs.python.org/3/) for details on `while` loops and string manipulation.
