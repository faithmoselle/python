"""
AUTHOR: Faith Paule
PROGRAM CODE: BCS13
DATE: S.Y. 2022-2023
==================================================
BCS13_Paule_MiniAct230505
LANGUAGE: Python 3
TECH STACK: Core Python (built-ins: dict, while loop, try-except, input/output)
PURPOSE: E-commerce shopping cart simulation with input validation
KEY FEATURES:
  - Dictionary-based item storage
  - Input validation (non-empty strings, positive floats)
  - Running total calculation
  - Receipt generation
==================================================
PROGRAM: SHOPPING CART
Create a program that allows a user to add items to their shopping cart. The user should be able to add items and their respective prices.
The program should also display the total cost of the items in the shopping cart.
Instructions:
1. Create an empty dictionary called shopping_cart to hold the items and their respective prices.
2. Use a while loop to allow the user to add items to the shopping cart.
3. Inside the while loop, use the input() function to ask the user for the item name and price. The item name should be a string, and the price should be a float.
4. Add the item and price to the shopping_cart dictionary.
5. After the user adds an item, display a message to confirm that the item was added to the shopping cart.
6. Ask the user if they want to add another item. If they do, continue the while loop. If they do not, exit the while loop.
7. After the user is finished adding items, display the total cost of the items in the shopping cart.

Here is an example output of the program:
Welcome to the online store! Let's start shopping!
Please enter the name of the item: T-shirt
Please enter the price of the item: 20.00
T-shirt was added to your shopping cart.

Do you want to add another item? (y/n): y
Please enter the name of the item: Jeans
Please enter the price of the item: 50.00
Jeans was added to your shopping cart.

Do you want to add another item? (y/n): n
Thank you for shopping with us! Your total cost is $70.00

Note:
1. Make sure to validate user input to ensure that the item name is not empty and that the price is a positive number.
2. If the user enters invalid input, display an error message and ask them to enter the information again.
3. Screenshot your solution code-based and results and paste in our sb lecture account

Grading:
	First 1-2 submission without errors --> 100 points
	Second 3-5 submission without errors --> 90 points
	Third 5-10 submission without errors --> 85
	the rest without errors --> 80
	Late submission or submission with error --> 60
"""

# Initialize empty dictionary (as required by instructions)
shopping_cart = {}

# Display welcome message and catalog
print("=" * 70)
print("Welcome to the FPau Online Store! Let's start shopping!")
print("=" * 70)
print("Items Available: ")
print("-" * 70)
print("Fresh Goods: \n  • Fish 1kg - ₱180.00 \n  • Meat 1kg - ₱200.00")
print("\nFrozen Goods: \n  • Nuggets - ₱300.00 \n  • TJ Hotdog - ₱140.00\n  • Ham - ₱350.00")
print("\nVegetables: \n  • Carrots - ₱50.00 \n  • Potatoes - ₱40.00\n  • Lettuce - ₱70.00")
print("\nToiletries: \n  • Detergent - ₱100.00 \n  • Bar Soap - ₱40.00\n  • Shampoo - ₱200.00")
print("=" * 70)

# Get customer name (store in variable for later use)
customer_name = input("\nCustomer Name: ")

# Main shopping loop
while True:
    # Ask user if they want to add an item
    add_more = input("\nDo you want to add an item? (Y/N): ").capitalize()
    
    # Exit condition
    if add_more == 'N':
        print(f"\nThank you for shopping with us, {customer_name}!")
        break
    
    # Invalid input handling
    if add_more != 'Y':
        print("X Invalid input. Please enter 'Y' for Yes or 'N' for No.")
        continue
    
    # Get item name with validation (non-empty)
    while True:
        item = input("Please enter the name of the item: ").strip()
        if item:  # Check if not empty
            break
        print("X Error: Item name cannot be empty. Please try again.")
    
    # Get item price with validation (positive number)
    while True:
        try:
            price = float(input("Please enter the price of the item: ₱"))
            if price > 0:
                break
            print("X Error: Price must be a positive number. Please try again.")
        except ValueError:
            print("X Error: Invalid input. Please enter a numeric value.")
    
    # Add item to dictionary (as required by instructions)
    shopping_cart[item] = price
    print(f"✓ {item} was added to your shopping cart.")
    
    # Display current shopping cart contents
    print("=" * 70)
    print("Current Shopping Cart:")
    if shopping_cart:
        for item_name, item_price in shopping_cart.items():
            print(f"  • {item_name}: ₱{item_price:.2f}")
    print("=" * 70)

# Calculate total cost by summing all prices in dictionary
total_cost = sum(shopping_cart.values())

# Display final receipt and total
print("=" * 70)
print("RECEIPT")
print("=" * 70)
print(f"Customer: {customer_name}")
print("-" * 70)
for item, price in shopping_cart.items():
    print(f"{item:<30} ₱{price:>8.2f}")
print("-" * 70)
print(f"{'TOTAL AMOUNT DUE:':<30} ₱{total_cost:>8.2f}")
print("=" * 70)
print("Thank you for shopping with us! Come again soon!")
