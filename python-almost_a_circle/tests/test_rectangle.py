#!/usr/bin/python3
"""Unittest for Rectangle class"""
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """
    tests methods of Rectangle class
    """

    def test_values(self):
        """check width, height, x, y and id with ints"""
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)

        r2 = Rectangle(10, 2, 1, 1, 12)
        self.assertEqual(r2.width, 10)
        self.assertEqual(r2.height, 2)
        self.assertEqual(r2.x, 1)
        self.assertEqual(r2.y, 1)
        self.assertEqual(r2.id, 12)

    def test_validation(self):
        """test values with negatives and not ints"""
        with self.assertRaises(TypeError):
            Rectangle()
        with self.assertRaises(TypeError):
            Rectangle(None)
        with self.assertRaises(TypeError):
            Rectangle("10", 2, 1, 1)
        with self.assertRaises(TypeError):
            Rectangle(10, {2}, 1, 1)
        with self.assertRaises(TypeError):
            Rectangle(10, 2, (1, 3, 3), 1)
        with self.assertRaises(TypeError):
            Rectangle(10, 2, 1, [1])
        with self.assertRaises(ValueError):
            Rectangle(-10, 2, 1, 1)
        with self.assertRaises(ValueError):
            Rectangle(0, 2, 1, 1)
        with self.assertRaises(ValueError):
            Rectangle(10, -2, 1, 1)
        with self.assertRaises(ValueError):
            Rectangle(-10, 0, 1, 1)
        with self.assertRaises(ValueError):
            Rectangle(10, 2, -1, 1)
        with self.assertRaises(ValueError):
            Rectangle(10, 2, 1, -1)

    def test_area(self):
        """check area"""
        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6)

        r2 = Rectangle(2, 10)
        self.assertEqual(r2.area(), 20)

        r3 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r3.area(), 56)

    def test_str(self):
        """check str representation"""
        r1 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(r1.__str__(), '[Rectangle] (12) 2/1 - 4/6')

    def test_update_args(self):
        """check the method update with *args"""
        r6 = Rectangle(10, 2, 3, 4, 12)
        r6.update(2)
        self.assertEqual(r6.__str__(), "[Rectangle] (2) 3/4 - 10/2")
        r6.update(2, 15)
        self.assertEqual(r6.__str__(), "[Rectangle] (2) 3/4 - 15/2")

    def test_update_kwargs(self):
        """check the method update with kwargs"""
        r7 = Rectangle(10, 2, 3, 4, 12)
        r7.update(height=9)
        self.assertEqual(r7.__str__(), "[Rectangle] (12) 3/4 - 10/9")
        r7.update(width=5, x=8)
        self.assertEqual(r7.__str__(), "[Rectangle] (12) 8/4 - 5/9")
        r7.update(y=11, width=22, x=33, id=89)
        self.assertEqual(r7.__str__(), "[Rectangle] (89) 33/11 - 22/9")

    def test_to_dictionary(self):
        """check dictionary"""
        r1 = Rectangle(10, 2, 3, 4, 12)
        r_dict = {'id': 12, 'width': 10, 'height': 2, 'x': 3, 'y': 4}
        self.assertEqual(r1.to_dictionary(), r_dict)

    if __name__ == "__main__":
        unittest.main()
