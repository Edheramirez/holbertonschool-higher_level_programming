#!/usr/bin/python3
"""
removes all characters c and C from a string
"""


def no_c(my_string):
    """define no c"""
    new_str = str()
    for character in my_string:
        if not (character == "c" or character == "C"):
            new_str += character
    return new_str
