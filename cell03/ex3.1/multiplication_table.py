#!/usr/bin/env python3

# Prompt the user to enter a number
number = int(input("Enter a number\n"))

# Display the multiplication table for the entered number
for i in range(10):
    print(f"{i} x {number} = {i * number}")
