from typing import Callable
import functools


def decorator_with_args_for_any_decorator(decorator: Callable) -> Callable:
	def dec(*args, **kwargs):
		def wrapped(func: Callable):
			def func_args(f, s):
				print(args, kwargs)
				decorator(func, f, s)
			return func_args
		return wrapped
	return dec



@decorator_with_args_for_any_decorator
def decorator(func: Callable, *args, **kwargs):
	@functools.wraps(func)
	def wrapped():
		return func(args, kwargs)
	return wrapped()

@decorator(100, 'рублей', 200, 'друзей')
def function(text: str, num: int) -> None:
	print("Привет", text, num)


function("Юзер", 101)

