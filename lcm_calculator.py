"""
AUTHOR: Faith Paule
DATE:

PROGRAM: LCM Calculator
LANGUAGE: Python 3
TOPIC: Basic Python - Mathematical Computing (GCD/LCM)

DESCRIPTION:
Calculates Least Common Multiple (LCM) of multiple integers
using the relation: LCM(a,b) = |a × b| ÷ GCD(a,b)
"""

def gcd(a, b):
    """
    Greatest Common Divisor using Euclidean algorithm.
    Example: gcd(12, 18) = 6
    """
    while b:
        a, b = b, a % b
    return abs(a)


def lcm(a, b):
    """
    Least Common Multiple of two numbers.
    Example: lcm(12, 18) = 36
    """
    return abs(a * b) // gcd(a, b)


def multiple_lcm(*args):
    """
    LCM of multiple numbers (2 or more).
    Example: multiple_lcm(4, 6, 8) = 24
    """
    if len(args) < 2:
        raise ValueError("MINIMUM of 2 numbers required")
    
    result = args[0]
    for num in args[1:]:
        result = lcm(result, num)
    return result


def get_user_input():
    """Get space-separated numbers. Type 'X' to exit."""
    try:
        input_str = input("Enter numbers separated by spaces. Type 'X' to terminate: ")
        if input_str.lower() == 'x':
            return None
        numbers = [int(x) for x in input_str.split()]
        return numbers
    except ValueError:
        print("\nInvalid input. Please enter valid integers.\n")
        return get_user_input()


def format_with_spaces(number):
    """Add commas for readability: 1000000 → 1,000,000"""
    return "{:,}".format(number)


def main():
    """Interactive LCM calculator with menu loop."""
    print("WELCOME TO THE LCM CALCULATOR PROGRAM!")

    while True:
        user_input = input("\nDo you want to calculate LCM? (Y/N): ").lower()
        if user_input != 'y':
            print("Program terminated.")
            break

        numbers = get_user_input()
        if numbers is None:
            print("Program terminated.")
            break

        result = multiple_lcm(*numbers)
        formatted_numbers = [format_with_spaces(num) for num in numbers]
        formatted_result = format_with_spaces(result)

        print(f"\nThe LCM of {', '.join(formatted_numbers)} is: {formatted_result}")

    print("Thank you for using the LCM Calculator!")


if __name__ == "__main__":
    main()
