#!/usr/bin/python3
"""define class"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class"""
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__width = size
        self.__height = size
        Rectangle.__init__(self, size, size)

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return "[Square] {}/{}".format(self.__width, self.__height)
