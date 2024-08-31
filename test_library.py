import unittest
from library import Book, Library
class TestLibraryManagementSystem(unittest.TestCase):
    
    # testcase for add_book() function    
    def test_add_book(self):
        # self.assertIsNotNone(library.add_book("abc"))
        self.library = Library()
        self.book1 = Book(1234567890,'book1','author1',2024)
        self.library.add_book(self.book1)
        
    def test_borrow_book(self):
        self.assertIsNotNone(borrow_book())
        
    
if __name__ == '__main__':
    unittest.main()