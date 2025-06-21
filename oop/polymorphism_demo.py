import math

class Shape:
    def area(self):
        """Raise NotImplementedError for base class area calculation."""
        raise NotImplementedError("Area calculation not implemented for base Shape class")

class Rectangle(Shape):
    def __init__(self, length, width):
        """Initialize a Rectangle with length and width."""
        self.length = length
        self.width = width

    def area(self):
        """Calculate the area of the Rectangle."""
        return self.length * self.width

class Circle(Shape):
    def __init__(self, radius):
        """Initialize a Circle with radius."""
        self.radius = radius

    def area(self):
        """Calculate the area of the Circle."""
        return math.pi * self.radius ** 2
