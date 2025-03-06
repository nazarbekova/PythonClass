
class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.grades = []

    def add_grade(self, grade):
        """Добавляет оценку в список grades."""
        self.grades.append(grade)

    def calculate_average(self):
        """Возвращает средний балл."""
        if self.grades:
            return sum(self.grades) / len(self.grades)
        else:
            return 0

    def get_best_grade(self):
        """Возвращает лучшую оценку."""
        if self.grades:
            return max(self.grades)
        else:
            return None

    def get_worst_grade(self):
        """Возвращает худшую оценку."""
        if self.grades:
            return min(self.grades)
        else:
            return None  

    def display_info(self):
        """Выводит информацию о студенте."""
        average = self.calculate_average()
        best_grade = self.get_best_grade()
        worst_grade = self.get_worst_grade()
        print(f"Имя: {self.name}, ID: {self.student_id}, Средний балл: {average:.2f}, "
              f"Лучшая оценка: {best_grade}, Худшая оценка: {worst_grade}")



student1 = Student("Жази", 101)
student2 = Student("Лиз", 102)
student3 = Student("Чолпон", 103)

student1.add_grade(5)
student1.add_grade(4)
student1.add_grade(2)

student2.add_grade(5)
student2.add_grade(5)
student2.add_grade(5)

student3.add_grade(3)
student3.add_grade(3)
student3.add_grade(5)

student1.display_info()
student2.display_info()
student3.display_info()
