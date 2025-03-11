#!/usr/bin/env python3

# Prompt user for a number
num = float(input("Give me a number: "))

# Check if the number is an integer or decimal
if num.is_integer():
    print("This number is an integer.")
else:
    print("This number is a decimal.")
