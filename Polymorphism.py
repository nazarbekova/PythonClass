from abc import ABC, abstractmethod
class Employee(ABC):
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    @abstractmethod
    def work(self):
        pass

    def display_info(self):
        print(f"Имя: {self.name}")
        print(f"Возраст: {self.age}")
        print(f"Зарплата: {self.salary}")

class Developer(Employee):
    def __init__(self, name, age, salary, programming_language):
        super().__init__(name, age, salary)
        self.programming_language = programming_language

    def work(self):
        print(f"{self.name} {self.programming_language}")

class Manager(Employee):
    def __init__(self, name, age, salary, team_size):
        super().__init__(name, age, salary)
        self.team_size = team_size

    def work(self):
        print(f"{self.name} Кобра который управляют командой из {self.team_size} змей")

dev = Developer("Айзада", 30, 80000, "скуф и получает денег просто")
mgr = Manager("Марал", 40, 90000, 10 )

print("Информация о разработчике:")
dev.display_info()
dev.work()

print("\nИнформация о менеджере:")
mgr.display_info()
mgr.work()
