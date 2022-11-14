import os

text = input("Введите строку: ")
path = input("Куда хотите сохранить документ? Введите последовательность папок (через пробел): ")
file_name = input("Введите имя файла: ") + ".txt"


def creating_path(path, file_name):
	temp = path.split()
	temp.append(file_name)

	temp = os.path.sep.join(temp)
	temp = os.path.abspath(f"/{temp}")
	return temp

def main(temp, text):
	if os.path.exists(temp[0:-1 + (-len(file_name))]):
		if os.path.isfile(temp):
			choose = input("Этот файл уже существует, вы уверены что хотите перезаписать файл? ")
			second_check(choose, temp, text)
		else:
			saving(temp, text)
	else:
		print("Директории не существует!")


def second_check(choose, temp, text):
	if choose.lower() == "да":
		saving(temp, text)
	else:
		print("Файл не сохранён!")


def saving(temp, text):
	file = open(temp, "w")
	file.write(text)
	file.close()
	print("Файл успешно сохранён!")


temp = creating_path(path, file_name)

main(temp, text)


# if os.path.exists(temp[0:-1 + (-len(file_name))]):
# 	if os.path.isfile(temp):
# 		choose = input("Этот файл уже существует, вы уверены что хотите перезаписать файл? ")
# 		if choose.lower() == "да":
# 			file = open(temp, "w")
# 			file.write(text)
# 			file.close()
# 			print("Файл успешно сохранён!")
# 		else:
# 			print("Файл не сохранён!")
# 	else:
# 		file = open(temp, "w")
# 		file.write(text)
# 		file.close()
# 		print("Файл успешно сохранён")
# else:
# 	print("Директории не существует!")
