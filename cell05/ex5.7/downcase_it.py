#!/usr/bin/env python3

import sys

def downcase_it():
    """
    Displays the given string in lowercase, or "none" if the number of parameters is not 1.
    """
    if len(sys.argv) == 2:
        print(sys.argv[1].lower())
    else:
        print("none")

if __name__ == "__main__":
    downcase_it()