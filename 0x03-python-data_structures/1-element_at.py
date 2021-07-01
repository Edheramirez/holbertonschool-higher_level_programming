#!/usr/bin/python3
"""retrieves an element from a list like in C"""


def element_at(my_list, idx):
    """def construct for element_at"""

    if idx < 0:
        return None
    if idx > len(my_list):
        return None
    return my_list[idx]
