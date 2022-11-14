

num = int(input("Введите число: "))

def count(end = num, start = 1):
	print(start)
	if start != end:
		count(start = start + 1)

count()

