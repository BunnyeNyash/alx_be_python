class Dog:
    def make_sound(self):
        """Dog's sound behavior."""
        print("Dog says Woof!")

class Cat:
    def make_sound(self):
        """Cat's sound behavior."""
        print("Cat says Meow!")

class Bird:
    def make_sound(self):
        """Bird's sound behavior."""
        print("Bird says Tweet!")

def let_them_speak(animals):
    """Call make_sound method on each object in the list."""
    for animal in animals:
        animal.make_sound()

# Test the polymorphic behavior
if __name__ == "__main__":
    dog = Dog()
    cat = Cat()
    bird = Bird()
    let_them_speak([dog, cat, bird])
