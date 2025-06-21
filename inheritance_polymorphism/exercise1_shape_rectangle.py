class Shape:
    def calculate_area(self):
        """Base method for calculating area."""
        print("Base shape area calculation not implemented.")

class Rectangle(Shape):
    def __init__(self, width, height):
        """Initialize a Rectangle with width and height."""
        self.width = width
        self.height = height

    def calculate_area(self):
        """Override to calculate the area of a rectangle."""
        area = self.width * self.height
        print(f"Area of Rectangle: {area}")

# Test the Shape and Rectangle classes
if __name__ == "__main__":
    shape = Shape()
    shape.calculate_area()

    rect = Rectangle(5, 3)
    rect.calculate_area()
