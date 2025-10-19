class Book:
    def __init__(self, title, author):
        """Base class for all books"""
        self.title = title
        self.author = author

    def __str__(self):
        """String representation of a basic book"""
        return f"Book: {self.title} by {self.author}"


class EBook(Book):
    def __init__(self, title, author, file_size):
        """Derived class for electronic books"""
        super().__init__(title, author)  # Call the base class constructor
        self.file_size = file_size

    def __str__(self):
        """String representation of an eBook"""
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


class PrintBook(Book):
    def __init__(self, title, author, page_count):
        """Derived class for printed books"""
        super().__init__(title, author)  # Call the base class constructor
        self.page_count = page_count

    def __str__(self):
        """String representation of a printed book"""
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


class Library:
    def __init__(self):
        """Composition: A library has a collection of books"""
        self.books = []

    def add_book(self, book):
        """Add a Book, EBook, or PrintBook instance to the library"""
        self.books.append(book)

    def list_books(self):
        """List all books in the library"""
        for book in self.books:
            print(book)
