#!/usr/bin/python3
"""function that prints a UTF-8 text file"""


def read_file(filename=""):
    """define class reads and prints a UTF-8 file"""
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
