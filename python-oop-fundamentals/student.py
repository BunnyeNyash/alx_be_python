class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        
    def display_info(self):
        print(f"Student: {self.first_name} {self.last_name}, Age: {self.age}")
