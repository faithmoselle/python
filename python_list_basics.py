"""
AUTHOR: Faith Moselle O. Paule
PROGRAM CODE: BCS13
DATE: S.Y. 2022-2023

PROGRAM: Python List Basics & Git Workflow Practice
LANGUAGE: Python 3
TOPIC: Basic Python - Strings, Lists, List Methods, Arithmetic Operations
TECH STACK: Python Standard Library

DESCRIPTION:
Demonstrates fundamental Python concepts including:
- String printing
- List creation and manipulation (append, remove, indexing)
- List methods (sort, reverse, len)
- Arithmetic operations (multiplication, addition)
- Comparison operators

GIT WORKFLOW PRACTICE:
- Stage modified files: git add <filename>
- Check status: git status
- Commit changes: git commit -m 'Add activity-solution session'
- Create private remote repo on GitHub
- Add collaborator: 'shewhocode8'
- Push to remote: git push origin main
"""
import math

# ============================================================================
# SECTION 1: BASIC PRINT STATEMENTS
# ============================================================================

print('I am String')  # Output: I am String

# ============================================================================
# SECTION 2: LIST CREATION AND DISPLAY
# ============================================================================

# List of BINI members (string elements)
myIdol = ['Aiah', 'Mikha', 'Maloi', 'Colet', 'Gwen', 'Sheena', 'Jhoanna', 'Stacey']
print(myIdol)  # Output: Full list of 8 members

# List of fruits (string elements)
myFruitBasket = ['apples', 'bananas', 'melon']
print(myFruitBasket)

# List of integers
listNumber = [11, 12, 8, 27]
# print(listNumber)  # Commented out

# List with mixed data types (string, int, bool, float)
myList = ['Joey', 30, True, 3.14]
print(myList)  # Output: ['Joey', 30, True, 3.14]

# ============================================================================
# SECTION 3: LIST INDEXING (0-based indexing)
# ============================================================================

# Accessing individual elements by their index position
# Python indexing starts at 0, so index 0 gives the first element
print(myList[0])  # Output: Joey

# ============================================================================
# SECTION 4: MODIFYING LIST ELEMENTS
# ============================================================================

# Reassign value at index 3 (originally 3.14) to 100
myList[3] = 100
print(myList)  # Output: ['Joey', 30, True, 100]

# ============================================================================
# SECTION 5: LIST METHODS - APPEND (add to end)
# ============================================================================

# .append() adds a new element to the end of the list
myList.append('BINI')
print(myList)  # Output: ['Joey', 30, True, 100, 'BINI']

# ============================================================================
# SECTION 6: LIST METHODS - REMOVE (delete by value)
# ============================================================================

# .remove() deletes the first occurrence of the specified value
myList.remove(True)  # Removes the boolean True from the list
print(myList)  # Output: ['Joey', 30, 100, 'BINI']

# ============================================================================
# SECTION 7: HELPER FUNCTIONS - len()
# ============================================================================

# len() returns the number of items in a list (built-in function)
print(len(myList))  # Output: 4 (elements: 'Joey', 30, 100, 'BINI')

# ============================================================================
# SECTION 8: LIST METHODS - SORTING
# ============================================================================

# .sort() arranges elements in ascending order (alphabetically for strings)
myIdol.sort()
print(myIdol)  # Output: ['Aiah', 'Colet', 'Gwen', 'Jhoanna', 'Maloi', 'Mikha', 'Sheena', 'Stacey']

# .sort(reverse=True) arranges in descending order
myIdol.sort(reverse=True)
print(myIdol)  # Output: ['Stacey', 'Sheena', 'Mikha', 'Maloi', 'Jhoanna', 'Gwen', 'Colet', 'Aiah']

# ============================================================================
# SECTION 9: STRING FORMATTING WITH LIST INDEXING
# ============================================================================

# Personal introduction using list elements
myIntroduction = ['Faith', 22, 'Netflix Programmer', 'Greys Anatomy', 8.0]

# Accessing multiple list elements by index for formatted output
print('I am ', myIntroduction[0], ', and I am ', myIntroduction[1],
      ' years old, I work as a ', myIntroduction[2], ', and my rating for ',
      myIntroduction[3], ' is ', myIntroduction[4], '%')

# ============================================================================
# SECTION 10: ARITHMETIC AND COMPARISON OPERATIONS
# ============================================================================
"""
ACTIVITY INSTRUCTIONS:
- Create 3 variables: num1, num2, and num3
- Get the product of num1 and num2
- Check if num1 is less than num3
- Add the value of num3 to num2
- Stage your modified file: git add <filename>
- Check status: git status
- Commit your file: git commit -m 'Add activity-solution session'
- Create remote repo 's03' on GitHub (PRIVATE)
- Add collaborator: 'shewhocode8'
- Push to remote: git push origin main
- Submit GitHub link to SB (Student Dashboard)
"""

# Variable declarations
num1 = 10
num2 = 20
num3 = 30

# Calculate product (multiplication)
product = num1 * num2
print(num1, 'x', num2, ' =', product)  # Output: 10 x 20 = 200

# Comparison operator - checks if num1 is less than num2
# Returns boolean True/False
print(num1, ' is less than ', num2, ' =', (num1 < num2))  # Output: True

# Addition operation
total = num3 + num2
print(num3, ' + ', num2, ' =', total)  # Output: 30 + 20 = 50

# ============================================================================
# GIT COMMANDS REFERENCE (run in terminal, not Python)
# ============================================================================
"""
# Navigate to project folder
cd /path/to/your/project

# Check Python version (terminal command, not Python code)
python --version

# Run Python script
python discussion.py

# Git workflow (terminal commands)
git add discussion.py          # Stage the file
git status                      # Check staging status
git commit -m 'Add activity-solution session'  # Commit changes
git remote add origin https://github.com/yourusername/s03.git  # Link remote
git push -u origin main         # Push to GitHub
"""
