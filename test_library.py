import unittest
from library import add_book

class TestLibraryManagementSystem(unittest.TestCase):
    
    # testcase for add_book() function    
    def test_add_book(self):
        # self.assertIsNotNone(add_book("abc"))
        self.book1=Book(1234567890,'book1','author1',2024)
        
    
if __name__ == '__main__':
    unittest.main()