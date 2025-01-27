#Write a Python Code to Generate Grades Using a Dictionary
def convert_to_grades(marks):
    if 90 <= marks <= 100:
        return 'A+'
    elif 80 <= marks < 90:
        return 'A'
    elif 70 <= marks < 80:
        return 'B'
    elif 60 <= marks < 70:
        return 'C'
    elif 50 <= marks < 60:
        return 'D'
    else:
        return 'F'

def generate_grades(students):
    grades = {}
    for student, subjects in students.items():
        grades[student] = {subject: convert_to_grades(mark) for subject, mark in subjects.items()}
    return grades

students = eval(input("Enter a dictionary with student names as keys and a dictionary of subject and marks as values: "))
grades = generate_grades(students)
print("Generated grades: " + str(grades))