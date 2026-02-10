# Parent class
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    # Method to display book details
    def display_book_details(self):
        print("Book Title:", self.title)
        print("Author:", self.author)


# Child class inheriting from Book
class IssuedBook(Book):
    def __init__(self, title, author, issued_to, issued_date):
        # Call parent class constructor
        super().__init__(title, author)
        self.issued_to = issued_to
        self.issued_date = issued_date

    # Method to display issued book details
    def display_issued_book_details(self):
        # Calling parent class method
        self.display_book_details()
        print("Issued To:", self.issued_to)
        print("Issued Date:", self.issued_date)


# Create object of IssuedBook
issued_book = IssuedBook(
    title="Python Programming",
    author="Guido van Rossum",
    issued_to="Alice",
    issued_date="10-Feb-2026"
)

# Display all details
issued_book.display_issued_book_details()
