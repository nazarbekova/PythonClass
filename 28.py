import math
import datetime


sqrt_value = math.sqrt(625) 
pi_value = math.pi        
cos_value = math.cos(math.radians(45)) 

print(f"Квадратный корень из 625: {sqrt_value}")
print(f"Значение числа π: {pi_value}")
print(f"Косинус угла 45 градусов: {cos_value}")


current_datetime = datetime.datetime.now()

try:
    with open("results.txt", "a") as file: 
        file.write(f"\nДата и время: {current_datetime}\n") 
        file.write(f"Квадратный корень из 625: {sqrt_value}\n")
        file.write(f"Значение числа π: {pi_value}\n")
        file.write(f"Косинус угла 45 градусов: {cos_value}\n")
except Exception as e:
    print(f"Ошибка при записи в файл: {e}")

try:
    with open("results.txt", "r") as file:
        print("\nСодержимое файла:")
        for line in file:
            print(line.strip())
except FileNotFoundError:
    print("Ошибка: файл 'results.txt' не найден.")
except Exception as e:
    print(f"Ошибка при чтении файла: {e}")



