import unittest
from library import Book, Library
class TestLibraryManagementSystem(unittest.TestCase):
    
    # this method is called before each testcase
    def setUp(self):
        self.library = Library()
        self.book1 = Book(1234567890123,'book1','author1',2024)
        self.book2 = Book(4567890123456,'book2','author2',2023)
        self.library.add_book(self.book1)
        self.library.add_book(self.book2)     
    
    # testcase for add_book() function    
    def test_add_book(self):
        # self.assertIsNotNone(add_book("abc"))  
        self.assertEqual(len(self.library.books), 2)
        self.assertEqual(self.library.books[0].title, 'book1')
        self.assertEqual(self.library.books[1].title, 'book2')
    
    # testcase to borrow book 
    def test_borrow_book(self):
        # self.assertIsNotNone(borrow_book())
        # self.assertTrue(borrow_book(1234567890123))
        self.library.borrow_book(1234567890123)
        self.assertTrue(self.book1.is_borrowed)
        
    # testcase to return book
    def test_return_book(self):
        # self.assertIsNotNone(return_book())
        # self.assertIsNotNone(return_book(1234567890123))
        self.library.return_book(1234567890123)
        self.assertFalse(self.book1.is_borrowed)
        self.library.borrow_book(1234567890123)
        self.library.return_book(1234567890123)
        self.assertFalse(self.book1.is_borrowed)
        
    def test_view_available_books(self):
        # self.assertIsNotNone(view_available_books(self))
        self.library.view_available_books()
        self.library.borrow_book(1234567890123)
        available_books = [book for book in self.library.books if not book.is_borrowed]
        self.assertEqual(len(available_books), 1)
        self.assertEqual(available_books[0].title, 'book2')
        
        
    
if __name__ == '__main__':
    unittest.main()