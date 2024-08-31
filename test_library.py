import unittest
from library import Book, Library, return_book
class TestLibraryManagementSystem(unittest.TestCase):
    
    # this method is called before each testcase
    def setUp(self):
        self.library = Library()
        self.book1 = Book(1234567890123,'book1','author1',2024)
    
    # testcase for add_book() function    
    def test_add_book(self):
        # self.assertIsNotNone(add_book("abc"))       
        self.library.add_book(self.book1)
    
    # testcase to borrow book 
    def test_borrow_book(self):
        # self.assertIsNotNone(borrow_book())
        # self.assertTrue(borrow_book(1234567890123))
        self.library.borrow_book(1234567890123)
        
    # testcase to return book
    def test_return_book(self):
        self.assertIsNotNone(return_book())
        
    
if __name__ == '__main__':
    unittest.main()