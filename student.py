
class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def calculate_average(self):
        if self.grades:
            return sum(self.grades) / len(self.grades)
        else:
            return 0

    def get_best_grade(self):
        if self.grades:
            return max(self.grades)
        else:
            return None

    def get_worst_grade(self):
        if self.grades:
            return min(self.grades)
        else:
            return None

    def display_info(self):
        print(f"Имя: {self.name}")
        print(f"ID студента: {self.student_id}")
        print(f"Оценки: {self.grades}")
        print(f"Средний балл: {self.calculate_average()}")


class StudentManager:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def display_all_students(self):
        for student in self.students:
            student.display_info()
            print("-" * 30)

    def get_top_student(self):
        top_student = max(self.students, key=lambda student: student.calculate_average())
        return top_student

    def get_lowest_student(self):
        lowest_student = min(self.students, key=lambda student: student.calculate_average())
        return lowest_student

student1 = Student("я", 101)
student1.add_grade(5)
student1.add_grade(4)
student1.add_grade(3)

student2 = Student("Марал", 102)
student2.add_grade(4)
student2.add_grade(4)
student2.add_grade(5)

student3 = Student("чолпон", 103)
student3.add_grade(2)
student3.add_grade(3)
student3.add_grade(4)

manager = StudentManager()
manager.add_student(student1)
manager.add_student(student2)
manager.add_student(student3)

print("Все студенты:")
manager.display_all_students()

top_student = manager.get_top_student()
print("Лучший студент:")
top_student.display_info()

worst_student = manager.get_lowest_student()
print("Студент с худшими оценками:")
worst_student.display_info()

