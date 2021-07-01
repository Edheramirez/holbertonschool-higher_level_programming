#!/usr/bin/python3
"""
prints all integers of a list, in reverse order
"""


def print_reversed_list_integer(my_list=[]):
    """define print revers list"""

    if not my_list:
        return

    for number in reversed(my_list):
        print("{:d}".format(number))
