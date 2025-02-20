# def my function(**kid):
# print("His last name is ")

# def my function(country="Norway")
#     p

# def my_function(x):
# # return (5 * x)
#     pass

# my_function(3)
# my_function(5)
# my_function(9)


# number = [12, 7, 34, 23, ]


# def evenFeven(args):
#     for i in args:
#         if i % 2 == 0:
#             print(i)
#         else:
#             print("odd")

# evenFeven(number)


# student = {"name":"Jenishgul", "age":"20", "grade": "A", "цвет":"карие"}
# print(student["цвет"])

# thistuple = ("abc", "hgc", "jbj")
# print(type(thistuple))


# fruits = ("apple", "bannan", "cherrry", "Ple")
# (green, *yello, red) = fruits
# print(red)
# print(green)
# print(yello)

# thisset = {"apple", "bannan", "hi", "cherrry",True, 1, 2, 3}
# thisset.add("orange")
# print(thisset)


# thisdict = {
#     "brand": "Ford"
#     "model": "Mustang"
#     "year": 1964 
# }
# print(thisdict)

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
        
# print(get_average_score("Bob", students))


def  find_top_student(students)