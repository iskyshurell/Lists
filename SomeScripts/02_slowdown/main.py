import time
from typing import Callable, Any

def delay_func(func: Callable) -> Callable:
	"""
	Декоратор который усыпляет функцию на 'timer' секунд
	"""
	def wrapped(*args: Any, **kwargs: Any) -> None:
		time.sleep(*args, **kwargs)
		return func()

	return wrapped


@delay_func
def some_func() -> None:
	print("Что-то происходит!")

delay = int(input("Сколько секунд нужно поспать? "))


some_func(delay)

