"""
AUTHOR: Faith Paule
DATE:
Previous file name: LabAct6

PROGRAM: Palindrome Checker
LANGUAGE: Python 3
TOPIC: Basic Python - String Manipulation

DESCRIPTION:
A palindrome is a word, sentence, verse, or number that reads 
the same backward and forward (e.g., "radar", "madam", "12321")
"""

# Explanation of palindrome
print("Palindrome is a word, sentence, verse, or even number that reads the same backward or forward.")

def isPalindrome(input):
    """
    Check if a string is a palindrome.
    Returns True if string reads same forward and backward.
    [::-1] reverses the string.
    """
    return input == input[::-1]  # Compare original with reversed

# Get user input
user_input = input("Enter a string or number: ")

# Call function to check palindrome
palindrome_result = isPalindrome(user_input)

# Display result
if palindrome_result:
    print("\tResult: PALINDROME")
else:
    print("\tResult: NOT PALINDROME")
