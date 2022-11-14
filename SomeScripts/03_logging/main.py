import datetime
from typing import Callable, Any
import os

def logging(func: Callable) -> Callable:
	def wrapper():
		try:
			print("Название функции {name}\tДокументация функции {doc}".format(
				name = func.__name__
				, doc = func.__doc__))

			return func()
		except Exception as exception:
			if not os.path.exists("errors.log"):
				open("errors.log", "w")

			with open("errors.log", "a", encoding = "utf-8") as error_file:
				error_file.write(f"Названиие функции: {func.__name__}, Имя ошибки: {type(exception).__name__}, Дата и время: {datetime.datetime.now()}\n")
				

	return wrapper

@logging
def my_func():
	"""
	ИЗИ
	"""

@logging
def error():
	raise TypeError


my_func()
error()
	
