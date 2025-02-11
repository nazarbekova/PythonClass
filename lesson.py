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
# letter = "p"s

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

# x = 5
# y = 1
# for i in range(1, 11):
#     for y in range (1, 11):
#         print(f"{x} x {y} ={x*y}")
#     print()
    
for i in range (1, 11):
    # for j in range(1, i + 1):
     print(" " .join(str(j) for j in range(1, i + 1)) )
     