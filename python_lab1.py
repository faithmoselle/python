"""
AUTHOR: Faith Moselle O. Paule
PROGRAM CODE: BCS13
DATE: S.Y. 2022-2023

LABORATORY ACTIVITY NO. 3 
Language: Python 3
Topic: Basic Python Programming - List Operations
Tech Stack: Python Standard Library

DESCRIPTION:
Creates a program that accepts 5 numbers from user input, stores them in a list,
then calculates and displays:
1. SUM of all numbers (using sum() function)
2. AVERAGE of all numbers (using len() function)
3. SMALLEST number in the list (using min() function)

"""

# ============================================================================
# STEP 1: Create an empty list to store numbers
# ============================================================================
my_list = []

# ============================================================================
# STEP 2: Accept 5 numbers from user using a for loop
# range(5) creates sequence: 0, 1, 2, 3, 4 (5 iterations)
# ============================================================================
for i in range(5):
    # Prompt user for input, convert string to integer
    num = int(input("Input Numbers: "))
    # Add the number to the end of the list
    my_list.append(num)

# ============================================================================
# STEP 3: Calculate statistics using built-in functions
# ============================================================================

# sum() - Adds all numbers in the list
total = sum(my_list)

# len() - Returns number of elements (5), used to calculate average
average = total / len(my_list)

# min() - Finds the smallest value in the list
smallest = min(my_list)

# ============================================================================
# STEP 4: Display the results
# ============================================================================

print("The sum of the list is:", total)
print("The average of the list is:", average)
print("The smallest number in the list is:", smallest)
