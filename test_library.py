import unittest
from library import add_book

class TestLibraryManagementSystem(unittest.TestCase):
    
    # testcase for add_book() function    
    def test_add_book(self):
        self.assertIsNotNone(add_book())
        
    
if __name__ == '__main__':
    unittest.main()