class Person:
    def __init__(self, name, age):
        """Initialize a Person with name and age."""
        self.name = name
        self.age = age

    @classmethod
    def create_child(cls, name):
        """Create a Person instance with age set to 0."""
        return cls(name, 0)

# Test the Person class
if __name__ == "__main__":
    person = Person("Alice", 30)
    child = Person.create_child("Bob")
    print(f"Person: {person.name}, Age: {person.age}")
    print(f"Child: {child.name}, Age: {child.age}")
