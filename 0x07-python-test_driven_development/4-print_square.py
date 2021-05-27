#!/usr/bin/python3
"""function to print a square"""


def print_square(size):
    """define class prints_square"""
    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    string = '#' * size
    for x in range(size):
        print(string)
