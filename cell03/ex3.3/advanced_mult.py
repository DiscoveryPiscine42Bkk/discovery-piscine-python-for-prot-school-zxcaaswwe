#!/usr/bin/env python3
import sys

# Check if an argument is passed and is not a number
if len(sys.argv) > 1 and not sys.argv[1].isdigit():
    print("none")
    sys.exit(0)

num = 0

# Outer loop for multiplication tables (0 to 10)
while num <= 10:
    table = f"Table de {num}:"
    multiplier = 0
    
    # Inner loop for each multiplication (0 to 10)
    while multiplier <= 10:
        table += f" {num * multiplier}"
        multiplier += 1
    
    print(table)
    num += 1
