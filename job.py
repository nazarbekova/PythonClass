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




# class Character:
#     def __init__(self, health, damage, speed):
#         self.health = health
#         self.damage = damage
#         self. speed = speed


#     def double_speed(self):
#         self.speed *= 2


# warrior = Character(100, 50, 20)
# ninja = Character(70, 30, 40)
       
 
# print(warrior.speed)
# print(ninja.speed)

# warrior.double_speed()

# print(f" Warrior New Speed {warrior.speed}")


class Employees:
    def __init__(self, name, last, salary):
        self.name = name
        self.last = last
        self.salary = salary
        self.email = name + "."+ last + "aman@gmail.com"

    def bonus(self):
        self.salary + 10000

emp1 = Employees("Aman", "Esen", 2000)

emp1.first = "Aman"
emp1.last = "Aman"
emp1.email = "aman@gmail.com"

print(emp1.salary)
emp1.bonus()
print(emp1.salary)
        

# library_books = {
#     "B001": {"title": "Основы Python", "borrower": "Алиса", "due_date": -5, "fine_rate": 0.50},
#     "B002": {"title": "Наука о данных", "borrower": "Боб", "due_date": 3, "fine_rate": 0.75},
#     "B003": {"title": "Введение в ИИ", "borrower": None, "due_date": 0, "fine_rate": 0.25},
#     "B004": {"title": "Алгоритмы", "borrower": "Алиса", "due_date": 2, "fine_rate": 1.00}
# }

# def calculate_fine(book):
#     overdue_days = book['due_date']
#     return max(0, -overdue_days) * book['fine_rate']

# def get_book_status(book):
#     if book['borrower'] is None:
#         return "Доступна"
#     elif book['due_date'] >= 0:
#         return "В срок"
#     else:
#         return "Просрочена"

# def get_highest_fine_borrower(library):
#     fines_by_borrower = {}
    
#     for book in library.values():
#         borrower = book['borrower']
#         fine = calculate_fine(book)
#         if borrower not in fines_by_borrower:
#             fines_by_borrower[borrower] = 0
#         fines_by_borrower[borrower] += fine

#     highest_fine_borrower = max(fines_by_borrower, key=fines_by_borrower.get)
#     return highest_fine_borrower, fines_by_borrower[highest_fine_borrower]

# def generate_report(library):
#     total_fine = 0 
    
#     for book_id, book in library.items():
#         fine = calculate_fine(book)
#         total_fine += fine
#         status = get_book_status(book)
#         print(f"Книга: {book['title']}, Статус: {status}, Штраф: ${fine:.2f}")
    
#     borrower, total_borrower_fine = get_highest_fine_borrower(library)
#     print(f"\nЗаемщик с наибольшими штрафами: {borrower} (${total_borrower_fine:.2f})")

#     print(f"\nОбщий штраф за просроченные книги: ${total_fine:.2f}")

# generate_report(library_books)


# class Car:
#     wheels = 4
#     def __init__(self):
        
#         print("Car is Driving")

# lambo = Car()

# lambo.drive()

