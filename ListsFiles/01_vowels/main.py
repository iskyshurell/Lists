vowels = ["а", "у", "о", "ы", "и", "э", "я", "ю", "ё", "е"]


text = input("Введите текст: ")

text_vowels = [i_sym for i_sym in text
               for i_elem in vowels
               if i_sym == i_elem]

print("Список гласных букв:", text_vowels)
print("Длина списка:", len(text_vowels))
