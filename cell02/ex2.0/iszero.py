#!/usr/bin/env python3

# Prompt the user to enter a number
number = input("")

# Convert input to an integer
try:
    number = int(number)
    if number == 0:
        print("This number is equal to zero.")
    else:
        print("This number is different from zero.")
except ValueError:
    print("Please enter a valid number.")
