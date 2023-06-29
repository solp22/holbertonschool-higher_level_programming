#!/usr/bin/python3
"""Unittest for Base class"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """
    tests methods for Base class
    """
    
    def test_id(self):
        """test id w int, negative, str empty and None"""
        b1 = Base()
        self.assertEqual(b1.id, 1)

        b2 = Base(12)
        self.assertEqual(b2.id, 12)

        b3 = Base(None)
        self.assertEqual(b3.id, 2)

        b4 = Base('a')
        self.assertEqual(b4.id, 'a')

        b5 = Base(-20)
        self.assertEqual(b5.id, -20)
    
    def test_to_json_string(self):
        """test method w list, empty and None"""
        list_dictionary = [{"x": 2, "width": 10}]
        json_dictionary = Base.to_json_string(list_dictionary)
        self.assertEqual(json_dictionary,'[{"x": 2, "width": 10}]')
        
        list_dictionary = []
        json_dictionary = Base.to_json_string(list_dictionary)
        self.assertEqual(json_dictionary, '[]')

        list_dictionary = None
        json_dictionary = Base.to_json_string(list_dictionary)
        self.assertEqual(json_dictionary, '[]')
    
    def test_from_json_string(self):
        """test method w list, empty and None"""
        list_dictionary = [{"x": 2, "width": 10}]
        json_list_input = Base.to_json_string(list_dictionary)
        list_output = Base.from_json_string(json_list_input)
        self.assertEqual(list_output, [{'x': 2, 'width': 10}])

        list_dictionary = []
        json_list_input = Base.to_json_string(list_dictionary)
        list_output = Base.from_json_string(json_list_input)
        self.assertEqual(list_output, [])

        list_dictionary = None
        json_list_input = Base.to_json_string(list_dictionary)
        list_output = Base.from_json_string(json_list_input)
        self.assertEqual(list_output, [])

