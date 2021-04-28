#!/usr/bin/python3
def print_last_digit(number):
    lastdig = int(repr(number)[-1])
    print(lastdig, end="")
    return lastdig
