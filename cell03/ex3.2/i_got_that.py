#!/usr/bin/env python3

# Infinite loop to accept user input
while True:
    user_input = input("What you gotta say? : ")
    if user_input.strip().upper() == "STOP":
        break
    print("I got that! Anything else?")
