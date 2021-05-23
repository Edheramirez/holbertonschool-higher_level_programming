#!/usr/bin/python3
"""A rectangle with a width and height"""


class Rectangle:
    """A class rectangle with seizes"""
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initialize values for, width, height"""

        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1
        """increasse instances"""

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

    def area(self):
        """Returns area of Rectangle"""
        area = self.__width * self.__height
        return area

    def perimeter(self):
        """Returns area of Rectangle"""
        if self.__width == 0 or self.__height == 0:
            perimeter = 0
        else:
            perimeter = self.__width * 2 + self.__height * 2
        return perimeter

    def __str__(self):
        """print rectangle whit #"""
        if self.__width == 0 or self.__height == 0:
            return ""
        string = ""

        for i in range(self.height):
            newline = '\n' if i != self.height - 1 else ""
            string += "#" * self.width + newline
        return string

    def __repr__(self):
        """representation rectangle whit #"""
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """message when rectangle it´s deleted and decreasse instances"""
        print("Bye rectangle...")
        if Rectangle.number_of_instances != 0:
            Rectangle.number_of_instances -= 1
