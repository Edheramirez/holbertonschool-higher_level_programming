#!/usr/bin/python3
"""Defines size for 0-square"""


class Square:
    """Define class type Square"""

    def __init__(self, size=0, position=(0, 0)):
        """private instance attribute"""
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """getter calls the position"""
        return self.__position

    @position.setter
    def position(self, value):
        """set position in the square"""
        if (type(value) != tuple or len(value) != 2 or
                type(value[0]) is not int or
                type(value[1]) is not int or
                value[0] < 0 or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """calculare area of square"""
        return (self.__size)**2

    def my_print(self):
        """print square whit #"""
        if self.__size == 0:
            print('')
        else:
            print('\n' * self.position[1], end='')
            for y in range(0, self.__size):
                print(' ' * self.position[0], end='')
                for x in range(0, self.__size - 1):
                    print('#', end='')
                print('#')
