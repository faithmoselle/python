"""
AUTHOR: Faith Moselle O. Paule
DATE:
Previous file name: LabAct3

LABORATORY ACTIVITY NO.5
LANGUAGE: Python 3
TOPIC: Basic Python - Dictionary Operations

Part 1: Sum of dictionary values
Part 2: Product of dictionary values
"""

my_dict = {'a': 25, 'b': 5, 'c': 100, 'd': 11, 'e': 12, 'f': 40}

# Display all values
values = my_dict.values()
print("Items in the dictionary: ", values)


# ========== PART 1: SUM ==========
def Sum(dict):
    """Calculate and print sum of all dictionary values."""
    addend = dict.values()      # Extract values (25,5,100,11,12,40)
    total = sum(addend)          # Built-in sum: 25+5+100+11+12+40 = 193
    print("\nPart 1\nSum of all values in the dictionary: ", total)

Sum(my_dict)


# ========== PART 2: PRODUCT ==========
def Product(dictionary):
    """Calculate and print product of all dictionary values."""
    elements = dictionary.values()  # Extract values
    multiplier = 1                   # Initialize (multiplication identity)
    
    for i in elements:               # Multiply each value
        multiplier = multiplier * i  # 1*25*5*100*11*12*40
    
    print("\nPart 2\nProduct of all values in the dictionary: ", multiplier)

Product(my_dict)
