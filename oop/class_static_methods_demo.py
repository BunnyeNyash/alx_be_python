class Calculator:
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """Return the sum of a and b."""
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """Print calculation_type and return the product of a and b."""
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
