#!/usr/bin/python3
class Rectangle:
    """A rectangle with a width and height"""

    def __init__(self, width=0, height=0):
        """Initialize values for, width, height"""

        self.height = height
        self.width = width


    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        """take value for width"""
        if not type(value) is int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        """Use decorators for validate width"""

        self.__width = value
        """evaluate and gives values for width"""

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        """take value for height"""
        if not type(value) is int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        """Use decorators for validate height"""

        self.__height = value
        """evaluate and gives values for height"""
