"""
AUTHOR: Faith Paule
DATE:
Previous file name: LabExam

LABORATORY EXAM
LANGUAGE: Python 3
TOPIC: Fibonacci Sequence with Square Calculation

REQUIREMENTS:
- Generate Fibonacci sequence in list format
- Accept only positive integers
- Display sequence and squares
"""

def fibonacci_series(n):
    """
    Generates Fibonacci sequence of n numbers.
    
    Args:
        n: Positive integer (number of Fibonacci numbers to generate)
    
    Returns:
        List containing Fibonacci sequence starting from [0, 1]
    """
    # Initialize with first two Fibonacci numbers
    fib_sequence = [0, 1]
    
    # Generate remaining numbers
    for i in range(2, n):
        next_num = fib_sequence[i - 1] + fib_sequence[i - 2]
        fib_sequence.append(next_num)
    
    return fib_sequence


# ========== INPUT VALIDATION ==========
# Loop until user enters a valid positive integer
while True:
    try:
        num = int(input("Enter the number of Fibonacci numbers: "))
        if num > 0:
            break
        else:
            print("Invalid input. Please enter a positive integer.")
    except ValueError:
        print("Invalid input. Please enter an integer.")


# ========== GENERATE FIBONACCI SEQUENCE ==========
fib_sequence = fibonacci_series(num)


# ========== DISPLAY RESULTS ==========
print("\nFibonacci sequence of", num, "numbers:")
print("fib_sequence:", fib_sequence)

print("\nFibonacci numbers with their squares:")
for i in range(1, num + 1):
    number = fib_sequence[i - 1]
    square = number ** 2
    print(f"Fibonacci number({i}): {number}, Square: {square}")
