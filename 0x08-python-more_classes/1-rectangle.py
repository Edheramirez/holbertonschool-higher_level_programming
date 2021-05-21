#!/usr/bin/python3
"""A rectangle with a width and height"""


class Rectangle:
    """A class rectangle with seizes"""

    def __init__(self, width=0, height=0):
        """Initialize values for, width, height"""

        self.height = height
        self.width = width


    @property
    def width(self):
        """getter calls the value"""
        return self.__width

    @width.setter
    def width(self, value):
        """take value for width"""

        if not type(value) is int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """getter calls the value"""
        return self.__height

    @height.setter
    def height(self, value):
        """take value for height"""
        if not type(value) is int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value
