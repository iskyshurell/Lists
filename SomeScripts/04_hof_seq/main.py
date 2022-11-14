class Q():
	def __init__(self, numbers):
		self.numbers = numbers[:]

	def __next__(self):

		try:
			new_num = self.numbers[len(self.numbers) - self.numbers[len(self.numbers) - 1]] + self.numbers[len(self.numbers) - self.numbers[len(self.numbers) - 2]]
			self.numbers.append(new_num)
			return new_num
		except IndexError:
			raise StopIteration()

	def __iter__(self):
		return self

a = Q([1, 1])
for i in range(10):
	print(a.__next__(), end = " ")
