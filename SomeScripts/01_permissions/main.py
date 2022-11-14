import functools
from typing import Callable

user_permissions = ['admin']

def check_permission(user: str = "guest") -> Callable:
	def dec_func(func: Callable) -> Callable:
		@functools.wraps(func)
		def wrapped():

			try:
				if user not in user_permissions:
					raise PermissionError("У вас недостаточно прав для выполнения этого действия!")
				else:
					func()
			except PermissionError as perm:
				print(f"{perm}\n")

		return wrapped
	return dec_func
		

@check_permission('admin')
def delete_site():
	print('Удаляем сайт')

@check_permission('user_1')
def add_comment():
	print("Коментарий оставлен")


delete_site()
add_comment()

