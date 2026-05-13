''''
PROGRAM:Student Grade Calculator

LANGUAGE: Python 3
TOPIC: Basic Python - Loops, Dictionaries, Conditional Statements, Weighted Averages
TECH STACK: Python Standard Library
==================================================
Machine Problem: 
Objective:
Write a Python program that accepts the grades of five students, such as Class participation composed of 5 Enabling Assessment, three (3) Summative Assessment, Final Examination and calculates their grade. The program should display the name of the student, average grade and the corresponding letter grade for each student based on the following grade system:

Formula:
Grade  = (Class participation * 30%) + (Summative Assessment * 30%) + (Final Examination * 40%)

Grade Score	Letter Grade
90 - 100	A
80 - 89	    B
70 - 79	    C
60 - 69	    D
Below 60	F
 
Requirements:

The program should prompt the user to enter the grades of five students.
The program should use a for loop to read the grades of each student using the input
The program should use if-elif-else statements to calculate the letter grade for each student based on the grading system above.
The program should calculate the grade of the five student and display it along with the corresponding letter grade based on the grading system above.
The program should used formatted output to display the results.
Stretch goal: 
Show the result in a table form

Rubrics:
Requirement	Points
Prompts the user to enter the grades of five students	5
Use a for loop to read the grades of each students using input function	5
Use if-elif-else statement to calculate the letter grade for each student based on the grading system	20
Calculate the grade based on the given formula of the students	25
Display the grade and the corresponding letter grade for each student based on the grading system and use the formatted output to display the result	20
Code readability	10
Code efficiency and elegance	5
Stretch Goal	10
Total Machine Problem Grade	100
 

Go to Module Lab SB:
    -copy the url of the home page for your s05/activity repo (URL on browser not the URL from clone button) and link it to our SB lab discussion:
'''
# Initialize empty dictionary to store student data
# Key: student name, Value: tuple of (average_grade, letter_grade)
students = {}

# Main loop - process exactly 5 students
for i in range(5):
    print(f"\n{'='*40}")
    print(f"Student {i+1} of 5")
    print(f"{'='*40}")
    
    # Get student name
    name = input(f"Enter student name: ")
    
    # Initialize accumulators for each grade component
    cp_total = 0      # Class participation total
    sa_total = 0      # Summative assessment total
    fe_score = 0      # Final exam score

    # ========== 1. CLASS PARTICIPATION (5 assessments) ==========
    # Each assessment contributes equally to the CP average
    for assessment_num in range(5):
        cp_total += float(input(f"  Class participation {assessment_num + 1}: "))
    
    # Calculate CP average and apply 30% weight
    cp_average = (cp_total / 5) * 0.3

    # ========== 2. SUMMATIVE ASSESSMENTS (3 assessments) ==========
    for assessment_num in range(3):
        sa_total += float(input(f"  Summative assessment {assessment_num + 1}: "))
    
    # Calculate SA average and apply 30% weight
    sa_average = (sa_total / 3) * 0.3

    # ========== 3. FINAL EXAMINATION (1 exam) ==========
    fe_score = float(input(f"  Final exam: "))
    
    # Apply 40% weight to final exam
    fe_weighted = fe_score * 0.4

    # ========== CALCULATE FINAL GRADE ==========
    # Formula: (CP_avg * 30%) + (SA_avg * 30%) + (FE * 40%)
    final_grade = cp_average + sa_average + fe_weighted

    # ========== DETERMINE LETTER GRADE ==========
    # Using if-elif-else ladder as required by rubric
    if final_grade >= 90:
        letter_grade = "A"
    elif final_grade >= 80:
        letter_grade = "B"
    elif final_grade >= 70:
        letter_grade = "C"
    elif final_grade >= 60:
        letter_grade = "D"
    else:
        letter_grade = "F"

    # Store student data in dictionary
    students[name] = (final_grade, letter_grade)

# ========== DISPLAY RESULTS IN TABLE FORMAT (STRETCH GOAL) ==========
print("\n")
print("=" * 45)
print("STUDENT GRADE REPORT")
print("=" * 45)
print(f"{'Student Name':<20} {'Final Grade':<15} {'Letter Grade':<10}")
print("-" * 45)

# Iterate through dictionary and display each student's results
for name, (average, letter) in students.items():
    # Formatted output with 2 decimal places for grade
    print(f"{name:<20} {average:>15.2f} {letter:>12}")

print("=" * 45)
print("End of Report")
