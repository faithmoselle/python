"""
AUTHOR: Faith Moselle O. Paule
PROGRAM CODE: BCS13
DATE: S.Y. 2022-2023

PROGRAM: Word Bank Program
FILE: word_bank_program.py
LANGUAGE: Python 3
TOPIC: Basic Python Programming - Lists, Loops, and User Input
TECH STACK: Python Standard Library

DESCRIPTION:
A word collection program that repeatedly asks users to enter words, stores them in a list, and finally displays the total count and all entered words. Useful for building vocabulary lists or data collection.

PROGRAM FLOW:
1. Initialize empty list and set loop control variable
2. While user wants to continue (Y/y):
   a. Ask for a word
   b. Add word to the list
   c. Ask if user wants to continue
3. Display total word count
4. Display all words in the list

AUTHOR: [Student Name]
DATE: [Current Date]
"""

# ============================================================================
# INITIALIZATION
# ============================================================================

# Initialize loop control variable - start with 'Y' to enter the loop
ans = "Y"

# Create an empty list to store words
# list() constructor creates a new empty list (same as [])
wordbank = list()

# ============================================================================
# MAIN COLLECTION LOOP
# ============================================================================

# While loop continues as long as user enters 'y' or 'Y'
# .lower() converts input to lowercase for case-insensitive comparison
while ans.lower() == "y":
    
    # Prompt user to enter a word
    # str() conversion is optional here since input() already returns string
    word = str(input("Enter a word: "))
    
    # Add the word to the end of the wordbank list
    wordbank.append(word)
    
    # Ask user if they want to continue
    # Stores 'y', 'Y', 'n', or 'N' for next loop iteration
    ans = str(input("Do you wish to try again? Y/N: "))

# ============================================================================
# DISPLAY RESULTS
# ============================================================================

# Print blank line for visual separation
print(" ")

# Display total number of words collected using len() function
print(f"Total number of words: {len(wordbank)}")

# Display header for the word list
print("Words in the list: ")

# Iterate through each word in wordbank and print it
# 'i' is a temporary variable that takes each word value
for i in wordbank:
    print(i)

# Program ends - all words displayed
