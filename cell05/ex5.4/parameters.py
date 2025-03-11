#!/usr/bin/env python3

import sys

def count_parameters():
    """
    Displays the number of command-line parameters passed to the script.
    """
    num_parameters = len(sys.argv) - 1  # Exclude the script name itself
    print(f"Number of parameters: {num_parameters}.")

if __name__ == "__main__":
    count_parameters()