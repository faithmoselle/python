"""
AUTHOR: Faith Moselle O. Paule
DATE:

PROGRAM: Ordered Pairs Generator (Cartesian Product)
FILE: ordered_pairs.py
LANGUAGE: Python 3
TOPIC: Basic Python - Nested Loops

DESCRIPTION:
Generates all ordered pairs (i, j) where i and j range from 1 to n.
Total pairs = n × n = n²
"""

def generate_pairs(n):
    """Generate all ordered pairs (i, j) for i,j in 1..n"""
    for i in range(1, n + 1):      # Outer loop: i from 1 to n
        for j in range(1, n + 1):  # Inner loop: j from 1 to n
            print(f"({i}, {j})")    # Print each pair


# Get user input
n = int(input("Enter n: "))
generate_pairs(n)
