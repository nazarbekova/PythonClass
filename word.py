# def capitalize_alternate_words(sentence):
#     words = sentence.split()
    
#     if len(words) < 2:
#         return "Too short to modify"
    
#     for i in range(0, len(words), 2):  
#         words[i] = words[i].capitalize()  
    
#     return " ".join(words)  

# sentence = "Я в университете"
# print(capitalize_alternate_words(sentence))



#   не четные
# x = 1         
# while x < 100:
#     if x % 2 != 0:
#         print(x)
#     # x += 1
#     x = x + 1


# number = [12, 7, 34, 23, 45, 66, 89, 90, 41, 55]
# even_numbers = []
# odd_number = []

# for x in number:
#     even_numbers.append(x)
# else:
#     odd_number.append(x)

# print(f"Четные числа: {even_numbers}")
# print(f"Нчетные числа: {odd_number}")


# оценка = input("список оценок : ").split()

# оценка = [int(grade) for grade in оценка]

# even_count = 0
# odd_count = 0

# for score in оценк:
   
#     if score >= 90:
#         letter_grade = 'A'
#         result = 'Сдал'
#     elif score >= 80:
#         letter_grade = 'B'
#         result = 'Сдал'
#     elif score >= 70:
#         letter_grade = 'C'
#         result = 'Сдал'
#     elif score >= 60:
#         letter_grade = 'D'
#         result = 'Сдал'
#     else:
#         letter_grade = 'F'
#         result = 'Не сдал'

#     print(f"Балл: {score} → Оценка: {letter_grade} ({result})")



students = [
 
 {
"name": "Alice",
  "subjects": ("Math", "Physics", "English"), 
  "scores": {"Math": 85, "Physics": 78, "English": 92}},
 {
"name": "Bob",
  "subjects": ("Math", "Biology", "English"), 
  "scores": {"Math": 72,"Biology": 88, "English": 80}},
 {
"name": "Charlie",
  "subjects": ("Math", "Physics", "Chemistry"), 
  "scores": {"Math": 90, "Physics": 95, "Chemistry": 85}},
]

def display_students(data):
    for student in data:
        name = student["name"]
        subject = ", ".join(student["subject"])
        print(f"{name} is enrolled in: {subject }")


# display_students(students)

def get_average_score(name, students):
    for student in students:
        if student["name"] == name:
            scores = student["scores"].values()
            return sum(scores) / len(scores) if scores else 0
    return None
        
print(get_average_score("Bob", students))