class Calculator:
    @staticmethod
    def add(a, b):
        """Return the sum of a and b."""
        return a + b

    @staticmethod
    def multiply(a, b):
        """Return the product of a and b."""
        return a * b

# Test the Calculator class
if __name__ == "__main__":
    print(f"Addition: {Calculator.add(5, 3)}")
    print(f"Multiplication: {Calculator.multiply(5, 3)}")
