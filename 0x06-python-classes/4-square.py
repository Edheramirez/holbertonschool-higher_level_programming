#!/usr/bin/python3
"""Defines size for 0-square"""


class Square:
    """Define class type Square"""

    def __init__(self, size=0):
        """private instance attribute"""
        self.size = size

    @property
    def size(self):
        """getter calls the value"""
        return self.__size

    @size.setter
    def size(self, value):
        """take value for size"""

        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """calculare area of square"""
        return (self.__size)**2
