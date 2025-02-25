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
        