#!/usr/bin/python3
"""define class"""


from models.base import Base


class Rectangle(Base):
    """Rectangle class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """initialize"""
        Base.__init__(self, id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """calculate area of rectangle"""
        return self.__height * self.__width

    def display(self):
        """print rectangle"""
        print("\n" * self.__y, end="")
        for i in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        return (f"[Rectangle] ({self.id}) "
                f"{self.x}/{self.y} - {self.width}/{self.height}")

    def update(self, *args):
        """assign argument to each attribute"""
        if len(args) > 4:
            self.__y = args[4]
        if len(args) > 3:
            self.__x = args[3]
        if len(args) > 2:
            self.__height = args[2]
        if len(args) > 1:
            self.__width = args[1]
        if len(args) > 0:
            self.id = args[0]
