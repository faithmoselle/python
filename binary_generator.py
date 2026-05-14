"""
AUTHOR: Faith Moselle O. Paule
DATE:

PROGRAM: Binary Number Generator (Power Set Range)
FILE: binary_generator.py
LANGUAGE: Python 3
TOPIC: Basic Python Programming - Loops and Binary Conversion
TECH STACK: Python Standard Library

DESCRIPTION:
Generates binary representations of all numbers from 0 to 2^n - 1.
This is useful for:
- Generating all possible binary strings of length n
- Power set enumeration (subset generation)
- Truth table generation for n variables

ALGORITHM:
1. Get n from user
2. Calculate 2^n (total numbers to generate)
3. For each number from 0 to 2^n - 1:
   - Convert to binary using bin()
   - Remove '0b' prefix using slicing [2:]
   - Print the binary representation

EXAMPLE:
n=3 → 2^3=8 numbers → binary from 0 to 7 (000 to 111)

TIME COMPLEXITY: O(2^n) - exponential growth
SPACE COMPLEXITY: O(n) for binary string storage
"""

# ============================================================================
# INPUT SECTION
# ============================================================================

# Get user input for the exponent value
n = input("Enter n: ")
n = int(n)  # Convert string to integer

# ============================================================================
# CALCULATE TOTAL NUMBERS
# ============================================================================

# ✅ CORRECTED: Use ** for exponentiation (power)
# Alternative: pow(2, n) or 1 << n (bit shift)
total_numbers = 2 ** n
print(f"Generating {total_numbers} binary numbers (0 to {total_numbers - 1})")
print("-" * 40)

# ============================================================================
# GENERATE AND PRINT BINARY NUMBERS
# ============================================================================

# ❌ ORIGINAL (WRONG): for i in range(0, 2 ^ n):
# ✅ CORRECTED: Use ** for exponentiation
for i in range(0, 2 ** n):
    # Convert integer to binary string
    # bin(i) returns something like '0b1010' for decimal 10
    # [2:] slices off the '0b' prefix, leaving just the binary digits
    binary_string = bin(i)[2:]
    print(binary_string)

# ============================================================================
# OPTIONAL: Formatted output with leading zeros
# ============================================================================

print("\n" + "=" * 40)
print("Formatted with leading zeros (length n):")
print("-" * 40)

for i in range(2 ** n):
    # zfill(n) pads with leading zeros to length n
    formatted_binary = bin(i)[2:].zfill(n)
    print(formatted_binary)
