"""
AUTHOR: Faith Moselle O. Paule
DATE:
Previous file name: LabAct3

PROGRAM: Sum of Digits
LANGUAGE: Python 3
TOPIC: Basic Python - Digit Manipulation

ALGORITHM:
1. Extract last digit using modulo (num % 10)
2. Add digit to total
3. Remove last digit using floor division (num //= 10)
4. Repeat until number becomes 0
"""

# Get integer from user
num = int(input("Enter a number: "))

total = 0  # Initialize sum accumulator

# Process each digit until number becomes 0
while num > 0:
    total += num % 10   # Add last digit to total
    num //= 10          # Remove last digit

# Display result
print("The sum of the digits: ", total)
