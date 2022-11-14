
class Square_Iter():
	def __init__(self, N: int)-> None:
		self.N = N
		self.cur_n = 0

	def __iter__(self):
		return self

	def __next__(self):
		if self.cur_n < self.N:
			self.cur_n += 1
			return self.cur_n ** 2

		else:
			raise StopIteration


def square_gen(N: int):
	for i in range(1, N + 1):
		yield i ** 2





N = int(input("Введите N число: "))

a = Square_Iter(N)
for i in a:
	print(i)

print()
for i in square_gen(N):
	print(i)

print()
generator = (i ** 2 for i in range(1, N + 1))
for i in generator:
	print(i)
