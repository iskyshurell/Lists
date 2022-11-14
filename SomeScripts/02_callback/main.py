import functools
from typing import Callable

app = {}
def callback(key) -> Callable:
	def dec_func(func: Callable):
		app[key] = func
		@functools.wraps(func)
		def wrapped():
			
			return func()
	return dec_func


@callback('//')
def example():
	print('Пример функции, которая возвращает ответ сервера')
	return 'OK'

route = app.get('//')
if route:
	response = route()
	print('Ответ:', response)
else:
	print('Такого пути нет')
