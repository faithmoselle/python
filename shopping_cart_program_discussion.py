"""
AUTHOR: Faith Paule
Program Code: BCS13
DATE: S.Y. 2022-2023
============================================================================
PROGRAM: Python Control Structures & Shopping Cart
FILE: python_control_structures_and_shopping_cart.py
LANGUAGE: Python 3
TOPIC: Basic Python Programming - Input/Output, Control Structures, Loops
TECH STACK: Python Standard Library

DESCRIPTION:
Comprehensive tutorial covering:
1. User input handling and type casting
2. Control structures (if-elif-else)
3. Loops (while, for)
4. Range() and enumerate() functions
5. Break statements
6. Shopping Cart implementation (dictionary-based)
"""

# ============================================================================
# SECTION 1: USER INPUT BASICS
# ============================================================================

# input() allows users to provide data to the program
# \n creates a new line for better formatting
userName = input("Please enter your username: \n")

# f-string formatting for cleaner output
print(f"Hello {userName}! Welcome to the Python Course!")

# Type casting: input() returns strings, convert to int for math operations
num1 = int(input("\nEnter 1st number: "))
num2 = int(input("Enter 2nd number: "))

# Without type casting, this would concatenate strings ("10" + "20" = "1020")
print(f"The sum of two numbers is {num1 + num2}")

# ============================================================================
# SECTION 2: CONTROL STRUCTURES - IF/ELSE STATEMENTS
# ============================================================================

"""
CONTROL STRUCTURES can be divided into:
a. SELECTION STRUCTURE (decision based on condition) - executes specific statements
   based on whether a condition is true or false.
   
   IF statement syntax:
   if <condition>:
       statements to execute if condition is true
   else:
       statements to execute if condition is false

b. REPETITION STRUCTURE (loops) - repeats code multiple times
   1. For loop - iterates over a sequence of values
   2. While loop - repeats as long as condition is true
"""

# Example 1: Simple if-else
num3 = 75

if num3 >= 60:
    print("\nCongratulations! You Passed the senior program")
else:
    print("\nThank you. You are not qualified to the senior program.")

# IMPORTANT: Python uses INDENTATION instead of curly braces {}
# Indentation distinguishes code blocks - must be consistent!

# Example 2: if-elif-else (elif = else if)
test_num = int(input("\nPlease enter a number: "))

if test_num > 0:
    print(f"{test_num} is a positive number.")
elif test_num == 0:
    print(f"{test_num} is zero.")
else:
    print(f"{test_num} is a negative number.")

# ============================================================================
# SECTION 3: MINI ACTIVITY - DIVISIBILITY CHECKER
# ============================================================================

"""
Mini Exercise: Determine if a number is divisible by 3, 5, or both.
- If divisible by 3 and 5: print "divisible by both"
- If divisible by 5: print "divisible by 5"
- If divisible by 3: print "divisible by 3"
- Otherwise: print "not divisible by 3 nor 5"
"""

print("\nMini-Activity")
numact = int(input("Enter a number: "))

# Check BOTH conditions first (more specific before general)
if numact % 3 == 0 and numact % 5 == 0:
    print(f"{numact} is divisible by both 3 and 5.")
elif numact % 5 == 0:
    print(f"{numact} is divisible by 5.")
elif numact % 3 == 0:
    print(f"{numact} is divisible by 3.")
else:
    print(f"{numact} is NOT divisible by 3 nor 5.")

# ============================================================================
# SECTION 4: LOOPS - WHILE LOOP
# ============================================================================

"""
WHILE LOOP syntax:
while condition:
    code to be executed while condition is true
    - condition is a boolean expression
"""

print("\nWhile Loop Example")
i = 1

while i <= 5:
    print(f"Current count {i}")
    i += 1  # Increment to avoid infinite loop

# WARNING: Infinite loop example (commented out)
# while False:  # Condition never true, loop won't execute
#     print('This will not run')
# To exit infinite loop: press Ctrl + C

# ============================================================================
# SECTION 5: LOOPS - FOR LOOP
# ============================================================================

"""
FOR LOOP syntax:
for element in sequence:
    code to be executed for each element
"""

print("\nFor Loop Example - Fruits")
fruits = ['apple', 'banana', 'cherry']

# 'in' keyword specifies the sequence to iterate over
for fruit in fruits:
    print(fruit)

# ============================================================================
# SECTION 6: RANGE() FUNCTION
# ============================================================================

# range(start, stop) - prints from start to stop-1
print("\nRange Function - Basic")
for count in range(1, 5):
    print(count)  # Output: 1, 2, 3, 4 (not 5)

# Range with custom start and stop
print("\nRange Function - Values 6 to 9")
for x in range(6, 10):
    print(f"The current value is {x}")

# Range with step increment (start, stop, step)
print("\nRange Function - With Step Increment")
for x in range(6, 20, 2):
    print(f"The current value is {x}")  # Output: 6, 8, 10, 12, 14, 16, 18

# ============================================================================
# SECTION 7: ENUMERATE() FUNCTION
# ============================================================================

# enumerate() returns both index AND value when iterating
print("\nEnumerate Function")
fruits = ['apple', 'banana', 'cherry']

for index, fruit in enumerate(fruits):
    print(index, fruit)  # Output: 0 apple, 1 banana, 2 cherry

# ============================================================================
# SECTION 8: BREAK STATEMENT
# ============================================================================

# break exits the loop immediately
print("\nBreak Statement Example")
j = 1

while j < 6:
    print(j)
    if j == 3:
        break  # Stops loop when j equals 3
    j += 1
# Output: 1, 2, 3 (then stops)

# ============================================================================
# SECTION 9: SHOPPING CART PROGRAM (CORRECTED VERSION)
# ============================================================================

"""
PROGRAM: SHOPPING CART
Instructions:
1. Create empty dictionary shopping_cart
2. Use while loop for adding items
3. Get item name (string) and price (float)
4. Add to dictionary
5. Confirm addition
6. Ask to continue
7. Display total cost at end
8. Validate: non-empty name, positive price
"""

# CORRECTED IMPLEMENTATION:
print("\n" + "="*70)
print("Welcome to the FPau Online Store! Let's start shopping!")
print("="*70)

# Display available items (enhancement)
print("\nItems Available:")
print("-"*70)
print("Fresh Goods: \n  • Fish 1kg - ₱180.00 \n  • Meat 1kg - ₱200.00")
print("\nFrozen Goods: \n  • Nuggets - ₱300.00 \n  • TJ Hotdog - ₱140.00\n  • Ham - ₱350.00")
print("\nVegetables: \n  • Carrots - ₱50.00 \n  • Potatoes - ₱40.00\n  • Lettuce - ₱70.00")
print("\nToiletries: \n  • Detergent - ₱100.00 \n  • Bar Soap - ₱40.00\n  • Shampoo - ₱200.00")
print("="*70)

# Get customer name
customer_name = input("\nCustomer Name: ")

# FIX 1: Use dictionary as required
shopping_cart = {}

# Main shopping loop
while True:
    # Ask if user wants to add an item
    add_more = input("\nDo you want to add an item? (Y/N): ").capitalize()
    
    # Exit condition
    if add_more == 'N':
        print(f"\nThank you for shopping with us, {customer_name}!")
        break
    
    # FIX 2: Handle invalid input without breaking
    if add_more != 'Y':
        print("X Invalid input. Please enter 'Y' for Yes or 'N' for No.")
        continue  # Re-prompt instead of breaking
    
    # FIX 3: Validate item name (non-empty)
    while True:
        item = input("Please enter the name of the item: ").strip()
        if item:
            break
        print("X Error: Item name cannot be empty. Please try again.")
    
    # FIX 4: Validate price (positive number)
    while True:
        try:
            price = float(input("Please enter the price of the item: ₱"))
            if price > 0:
                break
            print("X Error: Price must be a positive number.")
        except ValueError:
            print("X Error: Please enter a valid number.")
    
    # Add to dictionary
    shopping_cart[item] = price
    print(f"✓ {item} was added to your shopping cart.")
    
    # Display current cart contents
    print("\n" + "="*70)
    print("Current Shopping Cart:")
    if shopping_cart:
        for cart_item, cart_price in shopping_cart.items():
            print(f"  • {cart_item}: ₱{cart_price:.2f}")
    else:
        print("  (empty)")
    print("="*70)

# FIX 5: Calculate and display total ONCE at the end
if shopping_cart:
    total_cost = sum(shopping_cart.values())
    print("\n" + "="*70)
    print("RECEIPT")
    print("="*70)
    print(f"Customer: {customer_name}")
    print("-"*70)
    for item, price in shopping_cart.items():
        print(f"{item:<30} ₱{price:>8.2f}")
    print("-"*70)
    print(f"{'TOTAL AMOUNT DUE:':<30} ₱{total_cost:>8.2f}")
    print("="*70)
else:
    print("\nNo items were purchased. Thank you for visiting!")

print("\nThank you for shopping with us! Come again soon!")
