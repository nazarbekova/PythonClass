# def mask_card_number(card_number):
#     if len(card_number) == 16 and card_number.isdigit():
#         return '*' * 12 + card_number [-4:]
#     else:
#         return "Invalid card nomber"
    
# card_number = input("Ведите номер карты")
# print(mask_card_number(card_number))


# def find_words_with_letter(words, letter):
#     result = [word for word in words if word.count(letter) >= 3]
#     return result if result else "No words found"

# # Пример использования
# words = ["banana", "apple", "cherry", "grape","pineapple"]
# letter = "p"

# print(find_words_with_letter(words, letter))
# i = 1 
# while i < 6:
#    if i == 3:
#       continue
#    if i == 1
#    continue
# for x in "banana":
#     print(x)
# for x in range(1, 10, 2):
#     print(x)

# x = 5
# y = 1
# for x in range(1, 11):
#     for y in range (1, 11):
#         print(f"{x} x {y} ={x*y}")
#     print()


# Пирамида
# x = 5
# y = 1
# for i in range(1, 11):
#     for y in range (1, 11):
#         print(f"{x} x {y} ={x*y}")
#     print()
    
# for i in range (1, 11):
#     # for j in range(1, i + 1):
#      print(" " .join(str(j) for j in range(1, i + 1)) )
# x = 1
# # while x < 11:
#     print(x)
#     x += 1


# def remove_duplicates(lst):
#     seen = set()
#     result = []
    
#     for num in lst:
#         if num not in seen:
#             seen.add(num)
#             result.append(num)
    
#     return result

# lst = [1, 2, 2, 3, 4, 6, 4, 11, 333, 45, 5]
# print(remove_duplicates(lst))


# def capitalize_alternate_words(sentence):
#     words = sentence.split()
    
#     if len(words) < 2:
#         return "Too short to modify"
    
#     for i in range(0, len(words), 2):  
#         words[i] = words[i].capitalize()  
    
#     return " ".join(words)  

# sentence = "Я в университете"
# print(capitalize_alternate_words(sentence))


# Максимум минимум

# number = [22, 45, 67, 12, 89, 34, 55, 90, 1]
# top_number = number [0]
# no_number = number [0]
# for x in number:
#     if x > top_number:
#        top_number = x
#     if x < no_number:
#         no_number = x
     
# print(f"максимум: {top_number}")
# print(f"минимум: {no_number}")


# Подчет гласных и согласных


word =input ("Введите слово")
vowels = "aeiou"
vow_count = 0
con_count = 0
for letter in word.lower():
        if letter in vowels:
            vow_count += 1
        elif letter.isalpha():
            con_count += 1

print(f"Гласные:, {vow_count}")
print(f"Согласные:, {con_count}")