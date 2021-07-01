#!/usr/bin/python3
"""print all integers"""


def print_list_integer(my_list=[]):
    """define list integer"""

    if not my_list:
        return
    for number in my_list:
        # recorre lista
        if isinstance(number, int):
            # builtin isinstance veriica si es una instancia de la clase
            print(number)