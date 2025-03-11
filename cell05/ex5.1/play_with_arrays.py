#!/usr/bin/env python3

def play_with_arrays():
    """
    Creates a new array by adding 2 to each element of an original array and displays both.
    """
    original_array = [2, 8, 9, 48, 8, 22, -12, 2]
    new_array = []

    for value in original_array:
        new_array.append(value + 2)

    print("Original array:", original_array)
    print("New array:", new_array)

if __name__ == "__main__":
    play_with_arrays()