#!/usr/bin/env python3

# Define the correct password
password = "Python is awesome"

# Prompt the user to enter a password
user_input = input("Enter password: ")

# Check if the entered password matches
if user_input == password:
    print("ACCESS GRANTED")
else:
    print("ACCESS DENIED")
