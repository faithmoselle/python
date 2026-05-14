"""
AUTHOR: Faith Paule
DATE:
Previous file name: LabAct1

PROGRAM: List and Tuple Generator
LANGUAGE: Python 3
TOPIC: Basic Python - String splitting, Lists, Tuples
"""

# Get comma-separated input from user
user_input = input("Input some comma-separated numbers: ")

# Split string into list (split at commas)
# "3,5,7,23" → ["3", "5", "7", "23"]
num_list = user_input.split(',')

# Convert to tuple
num_tuple = tuple(num_list)

# Display results
print("List:", num_list)
print("Tuple:", num_tuple)
