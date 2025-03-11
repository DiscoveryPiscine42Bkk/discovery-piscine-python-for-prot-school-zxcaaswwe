#!/usr/bin/env python3

# Prompt the user to enter a number
number = int(input("Enter a number less than 25\n"))

# Check if the number is greater than 25
if number > 25:
    print("Error")
else:
    # Loop from the input number to 25
    for i in range(number, 26):
        print(f"Inside the loop, my variable is {i}")
