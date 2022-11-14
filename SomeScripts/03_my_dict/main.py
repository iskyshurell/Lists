

'''
MyDict - класс похожий на словарь

  методы:

	- setter() -- добаляет в "словарь" новое значение

	- getter() -- достаёт из "словаря" значение ключа

	- d_values(), d_keys() -- возвращают значения ключей
	  и соответсвенно ключи

	- d_pop() - удаляет элемент из "словаря" и возвращает его значение

	В методе __init__() -- инициализируеться сам словарь

Функция testing(): предназначена для проверки словаря
 и проверяет работоспособность всех методов словаря
'''

class MyDict():
	def __init__(self):
		self.__dictionary = []

	def setter(self, key, value):
		self.__dictionary.append((key, value))

	def gettter(self, key):
		for i_tuple in self.__dictionary:
			if key == i_tuple[0]:
				return i_tuple[1]
		return 0

	def d_values(self):
		return [i_tuple[1] for i_tuple in self.__dictionary]

	def d_keys(self):
		return [i_tuple[0] for i_tuple in self.__dictionary]

	def d_pop(self, key):
		for i_tuple in self.__dictionary:
			if key == i_tuple[0]:
				self.__dictionary.remove(i_tuple)
				return i_tuple
		return 0


def testing():
	dictionary = MyDict()
	dictionary.setter("A", 5)
	print(dictionary.gettter("A"))
	print(dictionary.d_values())
	print(dictionary.d_keys())
	print(dictionary.d_pop("A"))
	print(dictionary.gettter("A"))

testing()
