#!/usr/bin/python3
"""replaces an element of a list at a specific position"""


def replace_in_list(my_list, idx, element):
    """define construcor of replace list"""

    if idx < 0:
        return my_list
    if idx >= len(my_list):
        return my_list
    my_list[idx] = element
    return my_list
