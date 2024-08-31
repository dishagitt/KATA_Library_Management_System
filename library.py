# Book class to hold attributes of book
class Book:
    def __init__(self, isbn, title, author, publication_year):
        if not isinstance(isbn, int):
            raise ValueError("ISBN must be a positive integer.")
        
        if not isinstance(title, str):
            raise ValueError("Title must be a non-empty string.")
        
        if not isinstance(author, str):
            raise ValueError("Author must be a non-empty string.")
        
        if not isinstance(publication_year, int) or not (1000 <= publication_year <= 9999):
            raise ValueError("Publication year must be an integer between 1000 and 9999.")
        
        self.isbn = isbn
        self.title = title
        self.author = author
        self.publication_year = publication_year

books = []    # Initialized empty list

# Library class to perform operations on books
class Library:
    
    def __init__(self):
        self.books = [] #empty list to hold books in library
    
    # method to add book in library collection
    def add_book(self, book):
        self.books.append(book)
        return book

