"""
Exercise 3: Develop a function to check if a number is even or odd.

Instructions:

Define a function that takes one parameter, number.
Inside the function,check the remainder after dividing the number by 2 is equal to zero.
If the remainder is zero, the number is even. Print a message indicating the number is even.
If the remainder is not zero, the number is odd. Print a message indicating the number is odd.
"""

def even_or_odd(number):
  """Checks if a number is even or odd"""
  if not isinstance(number, int):              # input vaalidation ... the number MUST be an integer ... "10" 0r 3.5 will raise an error
        raise ValueError("Input must be an integer")
  if number % 2 == 0:
    print(f"The number {number} is an even number")
  else:
    print(f"The number {number} is an odd number")

# Usage
even_or_odd(10)   # Output: The number 10 is an even number
even_or_odd(5)    # Output: The number 5 is an odd number
even_or_odd(0)    # Output: The number 0 is an even number
even_or_odd(-4)   # Output: The number -4 is an even number
even_or_odd(-7)   # Output: The number -7 is an odd number
