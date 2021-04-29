#!/usr/bin/python3
import sys
if __name__ == "__main__":
    argulen = len(sys.argv)
    if (argulen == 1):
        print("0 arguments.")
    elif (argulen == 2):
        print("1 argument:")
    else:
        print("{:d} arguments:".format(argulen - 1))
    for argc in range(1, argulen):
        if (argulen > 1):
            print("{:d}: {:s}".format(argc, sys.argv[argc]))
