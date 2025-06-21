class Book:
    def __init__(self, title, author, pages):
        """Initialize a Book with title, author, and pages."""
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        """Return a user-friendly string representation of the Book."""
        return f"{self.title} by {self.author}, {self.pages} pages"

    def __repr__(self):
        """Return an official string representation of the Book."""
        return f"Book(title='{self.title}', author='{self.author}', pages={self.pages})"

# Test the Book class
if __name__ == "__main__":
    book = Book("Python 101", "Johny Boy", 200)
    print(book)  # Calls __str__
    print(repr(book))  # Calls __repr__
