#!/usr/bin/env python3
"""
removes all characters c and C from a string
"""

def no_c(my_string):
    new_string = [i for i in my_string if (i is not "c" and i is not "C")]
    return "".join(new_string)
