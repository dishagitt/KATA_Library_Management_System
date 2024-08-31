class Book:
    def __init__(self, isbn, title, author, publication_year):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.publication_year = publication_year

books = []

class Library:
    
    def __init__(self):
        self.books = []
    
    def add_book(self, book):
        self.books.append(book)
        return book

