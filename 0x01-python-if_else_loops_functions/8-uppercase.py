#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        asc = ord(str[i])
        if asc >= 97 and asc <= 122:
            asc = asc - 32
        print("{:c}".format(asc), end="")
    print()
