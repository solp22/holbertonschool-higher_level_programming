#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """
    tests methods for max_integer
    """

    def test_ordered(self):
        """test max integer with a ordered list"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
    
    def test_unordered(self):
        """test max integer with a unordered list"""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
    
    def test_negative(self):
        """test max integer with a negative value"""
        self.assertEqual(max_integer([1, 2, 3, 4, -4]), 4)

    def test_allnegatives(self):
        """test max integer with all negative values"""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
    
    def test_empty(self):
        """test max integer with a empty list"""
        self.assertEqual(max_integer([]), None)
    
    def test_one(self):
        """test max integer with only one value"""
        self.assertEqual((max_integer([4])), 4)
    
    def test_string(self):
        """test max integer with a string in the list"""
        self.assertRaises(TypeError, max_integer, [1, "test", 4, 2])

    if __name__ == '__main__':
        unittest.main()
