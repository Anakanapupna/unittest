import unittest
from get import *


class get_class_test(unittest.TestCase):
    """Module to test simple http get"""

    def test_get_successful(self):
        """Should get a Dad Joke"""
        request = https_get()
        self.assertTrue(request["status"]==200)

    def test_joke_exists(self):
        """Should get a Dad Joke"""
        request = https_get()
        self.assertTrue(len(request["joke"])>0)

    def test_joke_is_string(self):
        """Should get a Dad Joke"""
        request = https_get()
        self.assertTrue(isinstance(request["joke"], str))

if __name__ == '__main__':
    unittest.main()