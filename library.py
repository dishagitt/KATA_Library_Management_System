# Book class to hold attributes of book
class Book:
    def __init__(self, isbn, title, author, publication_year):
        if not isinstance(isbn, int):
            raise ValueError("ISBN must be a positive integer.")
        
        isbn_str=str(isbn)
        if len(isbn_str) != 13:
            raise ValueError("ISBN must be a numeric value and exactly 13 digits long.")
        
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
        self.is_borrowed = False

books = []    # Initialized empty list

# Library class to perform operations on books
class Library:
    
    def __init__(self):
        self.books = [] #empty list to hold books in library
    
    # method to add book in library collection
    def add_book(self, book):
        for book in self.books:
            if book.isbn==book.isbn:
                print(f"Book '{book.title}' is already in the library")
            else:
                self.books.append(book)
                print(f"Book '{book.title}' is added to library. ")
    
    # method to borrow book from library collection
    def borrow_book(self, isbn):
        for book in self.books:
            if book.isbn==isbn:
                if book.is_borrowed:
                    print(f"Sorry, the book '{book.title}' is already borrowed.")
                else:
                    book.is_borrowed = True
                    print(f"You have borrowed '{book.title}'.")
                return
        print("Sorry, the book with this ISBN is not available in the library.")
    
    # method to return book
    def return_book(self,isbn):
        for book in self.books:
            if book.isbn == isbn:
                if book.is_borrowed:
                    book.is_borrowed = False
                    print(f"Thank you for returning '{book.title}'.")
                else:
                    print(f"The book '{book.title}' was not borrowed.")
                return
        print("Sorry, the book with this ISBN is not in the library's records.")
    
    # method to view availble books
    def view_available_books(self):
        for book in self.books:
            print(f"{book.title}")
           
def main():
    library = Library()

    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Borrow Book")
        print("3. Return Book")
        print("4. View Available Books")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            isbn = input("Enter ISBN: ")
            title = input("Enter title: ")
            author = input("Enter author: ")
            year = input("Enter publication year: ")
            book = Book(isbn, title, author, year)
            library.add_book(book)

        elif choice == '2':
            isbn = input("Enter ISBN of the book to borrow: ")
            library.borrow_book(isbn)

        elif choice == '3':
            isbn = input("Enter ISBN of the book to return: ")
            library.return_book(isbn)

        elif choice == '4':
            library.view_available_books()

        elif choice == '5':
            print("Exiting the system.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
