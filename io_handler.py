def get_input():
    name = input("Enter the name of the student: ")
    age = input("Enter the age of the student: ")
    grade = input("Enter the grade of the student: ")
    return name, age, grade

def display_students(students):
    print("Name\tAge\tGrade")
    for student in students:
        print(f"{student[0]}\t{student[1]}\t{student[2]}")
