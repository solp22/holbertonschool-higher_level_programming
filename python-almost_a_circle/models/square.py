#!/usr/bin/python3
"""define class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """square class"""
    def __init__(self, size, x=0, y=0, id=None):
        """initialize class"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """prints square data"""
        return (f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}")

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """assign argument to each attribute"""
        if args:
            if len(args) > 3:
                self.y = args[3]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 1:
                self.height = args[1]
                self.width = args[1]
            if len(args) > 0:
                self.id = args[0]
        else:
            for key in kwargs:
                if key == "size":
                    self.height = kwargs.get(key)
                    self.width = kwargs.get(key)
                if key == "x":
                    self.x = kwargs.get(key)
                if key == "y":
                    self.y = kwargs.get(key)
                if key == "id":
                    self.id = kwargs.get(key)

    def to_dictionary(self):
        """dictionary representation"""
        return {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}
