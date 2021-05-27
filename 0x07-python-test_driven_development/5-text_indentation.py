#!/usr/bin/python3
"""function that separates sentences"""


def text_indentation(text):
    """define class text_identation"""
    if type(text) is not str:
        raise TypeError("text must be a string")
    switch = 0
    for i in text:
        if switch == 0:
            if i == ' ':
                continue
            else:
                switch = 1
        if switch == 1:
            if i == '?' or i == '.' or i == ':':
                print(i)
                print()
                switch = 0
            else:
                print(i, end="")
