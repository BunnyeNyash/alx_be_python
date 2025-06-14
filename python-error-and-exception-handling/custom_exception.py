class ValueTooHighError(Exception):
    """Custom exception for numbers greater than 100."""
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return f"Error: {self.value} is too high. Must be 100 or less."

try:
    number = float(input("Enter a number: "))
    if number > 100:
        raise ValueTooHighError(number)
except ValueTooHighError as e:
    print(e)
except ValueError:
    print("Error: Please enter a valid number!")
else:
    print(f"Success: {number} is valid.")
finally:
    print("Input validation completed.")
