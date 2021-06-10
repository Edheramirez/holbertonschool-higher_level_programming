#!/usr/bin/python3
"""class Rectangle that inherits from Base"""
from models.base import Base


class Rectangle(Base):
    """attributes down"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """define constructor and Private instance attributes of rectangle"""
        """line17thissupercallwithusethe logic of the init of the Base class"""
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.integer_validator("width", value)
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.integer_validator("height", value)
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.integer_validator("x", value)
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.integer_validator("y", value)
        self.__y = value
    """Assign each argument width, height, x and y to the right attribute"""

    def integer_validator(self, name, value):
        """validation of arguments"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0 and name in ("width", "height"):
            raise ValueError("{} must be > 0".format(name))
        if value < 0 and name in ("x", "y"):
            raise ValueError("{} must be >= 0".format(name))
