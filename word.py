# def capitalize_alternate_words(sentence):
#     words = sentence.split()
    
#     if len(words) < 2:
#         return "Too short to modify"
    
#     for i in range(0, len(words), 2):  
#         words[i] = words[i].capitalize()  
    
#     return " ".join(words)  

# sentence = "Я в университете"
# print(capitalize_alternate_words(sentence))


def remove_duplicates(lst):
    seen = set()
    result = []
    
    for num in lst:
        if num not in seen:
            seen.add(num)
            result.append(num)
    
    return result

lst = [1, 2, 2, 3, 4, 6, 4, 11, 333, 45, 5]
print(remove_duplicates(lst))