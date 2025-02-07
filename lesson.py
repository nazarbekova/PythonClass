# def mask_card_number(card_number):
#     if len(card_number) == 16 and card_number.isdigit():
#         return '*' * 12 + card_number [-4:]
#     else:
#         return "Invalid card nomber"
    
# card_number = input("Ведите номер карты")
# print(mask_card_number(card_number))


def find_words_with_letter(words, letter):
    result = [word for word in words if word.count(letter) >= 2]
    return result if result else "No words found"

# Пример использования
words = ["banana", "apple", "cherry", "grape"]
letter = "a"

print(find_words_with_letter(words, letter))