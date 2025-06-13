from student import Student
from product import Product

# Test Student class
student = Student("Alice", "Smith", 18)
student.display_info()

# Test Product class
product = Product("Phone", 500, 10)
print(f"Total value of {product.name} in stock: ${product.total_value()}")
