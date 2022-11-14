N = int(input("Введите количество дисков: "))


def move(n, x, y, z) :
	if n == 1:
		print("Переложить диск {A} cо стержня номер {B} на стержень номер {C}".format(A = n, B = x, C = z))
	else:
		move(n - 1, x, z, y)
		print("Переложить диск {A} cо стержня номер {B} на стержень номер {C}".format(A = n, B = x, C = z))
		move(n - 1, y, x, z)

move(N, 1, 2, 3)
