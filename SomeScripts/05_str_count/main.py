from typing import Callable



def counter(func: Callable) -> Callable:

	def wrapper(count: int = 0) -> int:
		count += 1
		func()
		print(count)
		return count

	return wrapper

@counter
def Func():
	print("TASK")

count = Func()
count = Func(count)

for i in range(10):
	count = Func(count)





