from student import Student
from io_handler import get_input, display_students

if __name__ == '__main__':
    while True:
        print("\n1. Add student\n2. Display all students\n3. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            name, age, grade = get_input()
            student = Student(name, age, grade)
            student.save_info()
            print("Student added successfully!")
        
        elif choice == '2':
            students = Student.get_info()
            display_students(students)
        
        elif choice == '3':
            print("Exiting program...")
            break
        
        else:
            print("Invalid choice, please try again.")
