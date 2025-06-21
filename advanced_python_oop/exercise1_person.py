class Person:
    def __init__(self, name, age):
        """Initialize a Person with name and age."""
        self.name = name
        self.age = age
        print(f"Created Person: {self.name}, {self.age} years old")

    def __del__(self):
        """Print a farewell message when the object is deleted."""
        print(f"Farewell, {self.name}!")

# Test the Person class
if __name__ == "__main__":
    person = Person("Alice", 30)
    print(f"Person details: {person.name}, {person.age}")
    del person  # Explicitly delete to trigger __del__
