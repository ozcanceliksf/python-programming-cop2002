# Exercise 7 - Student Grade Calculator
# COP2002 - Python Programming
# Ozcan Celik

def calculate_average(grades):
    """Calculate the average of a list of grades."""
    if not grades:
        return 0
    return sum(grades) / len(grades)

def get_letter_grade(average):
    """Return letter grade based on numeric average."""
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"

def get_student_grades():
    """Collect grades from user input."""
    grades = []
    print("Enter grades one by one. Type 'done' to finish.\n")

    while True:
        entry = input("Enter grade: ").strip()
        if entry.lower() == "done":
            break
        try:
            grade = float(entry)
            if 0 <= grade <= 100:
                grades.append(grade)
            else:
                print("Grade must be between 0 and 100.")
        except ValueError:
            print("Invalid input. Enter a number or 'done'.")

    return grades

def display_report(name, grades):
    """Display full grade report for a student."""
    print("\n" + "=" * 40)
    print(f"  GRADE REPORT — {name.upper()}")
    print("=" * 40)

    if not grades:
        print("No grades entered.")
        return

    average = calculate_average(grades)
    letter = get_letter_grade(average)

    print(f"Grades entered : {grades}")
    print(f"Highest grade  : {max(grades)}")
    print(f"Lowest grade   : {min(grades)}")
    print(f"Average        : {average:.2f}")
    print(f"Letter grade   : {letter}")
    print("=" * 40)

if __name__ == "__main__":
    student_name = input("Enter student name: ").strip()
    grades = get_student_grades()
    display_report(student_name, grades)
