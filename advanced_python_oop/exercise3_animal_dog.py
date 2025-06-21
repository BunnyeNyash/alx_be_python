class Animal:
    def __init__(self, name):
        """Initialize an Animal with a name."""
        self.name = name

    def eat(self):
        """Print that the animal is eating."""
        print(f"{self.name} is eating.")

    def sleep(self):
        """Print that the animal is sleeping."""
        print(f"{self.name} is sleeping.")

class Dog(Animal):
    def __init__(self, name, breed):
        """Initialize a Dog with a name and breed."""
        super().__init__(name)
        self.breed = breed

    def bark(self):
        """Print that the dog is barking."""
        print(f"{self.name} says Woof!")

# Test the Animal and Dog classes
if __name__ == "__main__":
    animal = Animal("Generic")
    animal.eat()
    animal.sleep()

    dog = Dog("Buddy", "Labrador")
    dog.eat()
    dog.sleep()
    dog.bark()
