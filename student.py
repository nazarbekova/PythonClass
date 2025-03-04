class Student:
    def __init__(self, name, student_id, grade):
        self.name = name
        self.student_id = student_id
        self.grade =[ ]
    
    def add_grade(self, grade):
        self.grade.append(grade)

    def calculate_average(self):
        average = sum(self.grade) / len(self.grade)
        return average
    
    def display_info(self):

        print(f"Student: {self.name},student_id: {self.student_id}, grade: {self.grade}") 

std = Student("Alice", 301, 80)
std2 = Student("Jon", 302, 90)
std3 = Student("Rob", 303, 70)
std.add_grade(80)
std.add_grade(85)
std.add_grade(90)
std.calculate_average()
std.display_info()
    