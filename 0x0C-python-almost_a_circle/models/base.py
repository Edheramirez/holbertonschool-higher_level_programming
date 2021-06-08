#!/usr/bin/python3
"""This class will be the “base” of all other classes in this project"""


class Base:
    """attributes down"""
    __nb_objects = 0

    def __init__(self, id=None):
        """define class init and it pass id atributes - methods down"""

        if id is not None:
            self.id = id
            """if id is not None, assign the public instance attribute id """
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
            """otherwise, increment __nb_objects and assign the new value to the public instance attribute id"""
