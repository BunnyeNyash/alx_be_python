class Book:
    total_books = 0  # Class variable to count instances

    def __init__(self, title, author):
        """Initialize a Book with title and author."""
        self.title = title
        self.author = author
        Book.total_books += 1

    @classmethod
    def display_total_books(cls):
        """Display the total number of books created."""
        print(f"Total books created: {cls.total_books}")

# Test the Book class
if __name__ == "__main__":
    book1 = Book("Python 101", "John Doe")
    book2 = Book("Learning OOP", "Jane Smith")
    Book.display_total_books()
