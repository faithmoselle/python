""" 
AUTHOR: Faith Paule
PROGRAM CODE: BCS13
DATE: S.Y. 2022-2023

PROGRAM: Simple Number Repetition Program
FILE: number_printer.py
LANGUAGE: Python 3
TOPIC: Basic Python Programming - Input and Loops
TECH STACK: Python Standard Library

DESCRIPTION:
A simple program that takes a number from the user and prints that same
number three times using a for loop.

PROGRAM FLOW:
1. Prompt user to enter a number
2. Convert the input string to an integer
3. Loop 3 times (i = 1, 2, 3)
4. Print the original number in each iteration

NOTE: This program demonstrates basic input handling and loop structures.
"""

# ============================================================================
# INPUT SECTION - Get number from user
# ============================================================================

# Get user input and convert to integer
# WARNING: Using 'input' as variable name shadows (overwrites) the built-in input() function
# It's better to use a different name like 'user_input' or 'number'
user_number = int(input("Enter a number: "))  # Using better variable name

# ============================================================================
# LOOP SECTION - Print the number 3 times
# ============================================================================

# For loop that runs 3 times (i = 1, then 2, then 3)
# range(1, 4) produces: 1, 2, 3 (stops before 4)
for i in range(1, 4):
    # Print the original number (not the loop counter)
    # This will execute 3 times, printing the same number each time
    print(user_number)
