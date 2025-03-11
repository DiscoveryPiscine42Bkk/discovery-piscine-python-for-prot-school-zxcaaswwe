#!/usr/bin/env python3

def play_with_arrays():
    """
    Creates a new set (to remove duplicates) by adding 2 to each element of the original array,
    but only processes values greater than 5.
    """
    original_array = [2, 8, 9, 48, 8, 22, -12, 2]
    new_set = set()  # Use a set to automatically remove duplicates

    for value in original_array:
        if value > 5:
            new_set.add(value + 2)

    print(original_array)
    print(new_set)  # Sets are inherently unordered

if __name__ == "__main__":
    play_with_arrays()