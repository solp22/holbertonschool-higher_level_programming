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
