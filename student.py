class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def save_info(self):
        with open('students.txt', 'a') as f:
            f.write(f"{self.name},{self.age},{self.grade}\n")

    @staticmethod
    def get_info():
        with open('students.txt', 'r') as f:
            lines = f.readlines()
        return [line.strip().split(',') for line in lines]
