"""
PROGRAM: Factorial Range Printer
LANGUAGE: Python 3
TOPIC: Basic Python - Loops and Factorial
"""

import math  # Import math module for factorial function

# Get user input
n = input("Enter n: ")
n = int(n)  # Convert to integer

# Print numbers from 1 to (n! - 1)
# Example: n=4 → 4! = 24 → prints 1 to 23
for i in range(1, math.factorial(n)):
    print(i)
