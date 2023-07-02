#!/usr/bin/python3
"""Unittest for Square class"""
import unittest
from models.square import Square


class Test_Square(unittest.TestCase):
    """unittests for the methods in class Square"""

    def test_values(self):
        """check width, height, x, y and id with ints"""
        s1 = Square(2)
        self.assertEqual(s1.size, 2)

        s2 = Square(2, 4)
        self.assertEqual(s2.width, 2)
        self.assertEqual(s2.height, 2)
        self.assertEqual(s2.x, 4)

        s3 = Square(2, 4, 6)
        self.assertEqual(s3.width, 2)
        self.assertEqual(s3.height, 2)
        self.assertEqual(s3.x, 4)
        self.assertEqual(s3.y, 6)

        s4 = Square(2, 4, 6, 8)
        self.assertEqual(s4.width, 2)
        self.assertEqual(s4.height, 2)
        self.assertEqual(s4.x, 4)
        self.assertEqual(s4.y, 6)
        self.assertEqual(s4.id, 8)

    def test_validation(self):
        """check values with negatives and not ints"""
        with self.assertRaises(TypeError):
            Square("10", 2, 0, 12)
        with self.assertRaises(TypeError):
            Square(10, [2, 5], 0, 12)
        with self.assertRaises(TypeError):
            Square(10, 2, {"k": 0}, 12)
        with self.assertRaises(TypeError):
            Square((10, 7), 2, 0, 12)
        with self.assertRaises(TypeError):
            Square(10, 2, "hello", 12)
        with self.assertRaises(TypeError):
            Square(10, 2, {0}, 12)
        with self.assertRaises(ValueError):
            Square(0, 0, 0, 12)
        with self.assertRaises(ValueError):
            Square(-10, -2, 0, 12)
        with self.assertRaises(ValueError):
            Square(-10, 2, -4, 12)

    def test_str(self):
        """check the method __str__"""
        s5 = Square(2, 4, 6, 8)
        self.assertEqual(s5.__str__(), "[Square] (8) 4/6 - 2")

    def test_area(self):
        """check the method area"""
        s6 = Square(6)
        self.assertEqual(s6.area(), 36)
        s7 = Square(8, 7, 2, 89)
        self.assertEqual(s7.area(), 64)

    def test_to_dictionary(self):
        """check the method dictionary"""
        s7 = Square(10, 2, 3, 12)
        representation = {'id': 12, 'size': 10, 'x': 2, 'y': 3}
        self.assertEqual(s7.to_dictionary(), representation)

if __name__ == "__main__":
    unittest.main()