"""
Exercise 2: Define a dictionary to store information about your favorite book, including title, author, and genre. Use the method to retrieve the genre.
"""

book = {
    "title": "The Da Vinci Code",
    "author": "Dan Brown",
    "genre": "Thriller"
}

# Retrieve the genre using the get() method
print(book.get("genre"))
