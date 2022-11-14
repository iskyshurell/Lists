alphabet = ["а", "б", "в", "г",
            "е", "ё", "ж", "з",
            "и", "й", "к", "л",
            "м", "н", "о", "п", "р",
            "с", "т", "у", "ф", "х",
            "ц", "ч", "ш", "щ", "ъ",
            "ы", "ь", "э", "ю", "я"]


text = input("Введите сообщение: ")
K = int(input("Введите сдвиг: "))

index = [
			   (  alphabet.index(i_sym) + K
			      if i_sym != " "
			        else " "
			       )
             for i_sym in text
	]
if " " in index:
	space = index.index(" ")
	index.remove(" ")

encrypted = [(alphabet[i_index]
              if i_index <= len(alphabet) - 1 and i_index != " "

              else
                alphabet[i_index - len(alphabet)]
				)

					for i_index in index]

if " " in index:
	encrypted.insert(space, " ")

print(encrypted)