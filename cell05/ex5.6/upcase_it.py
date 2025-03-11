#!/usr/bin/env python3

import sys

def upcase_it():
    """
    Displays the given string in uppercase, or "none" if the number of parameters is not 1.
    """
    if len(sys.argv) == 2:
        print(sys.argv[1].upper())
    else:
        print("none")

if __name__ == "__main__":
    upcase_it()