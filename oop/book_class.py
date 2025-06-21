class Book:
    def __init__(self, title, author, year):
        """Initialize a Book with title, author, and year."""
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """Print a message when the book is deleted."""
        print(f"Deleting {self.title}")

    def __str__(self):
        """Return a user-friendly string representation."""
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """Return an official string representation."""
        return f"Book('{self.title}', '{self.author}', {self.year})"
