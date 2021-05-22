#!/usr/bin/python3
"""Defines size for 0-square"""


class Square:
    """Define class type Square"""

    def __init__(self, size=0):
        """private instance attribute"""

        if type(size) is not int:
            raise TypeError("size must be an integer")
        """Evaluate if is not an integer"""

        if size < 0:
            raise ValueError("size must be >= 0")
        """Evaluate if the size it´s not 0"""

        self.__size = size
