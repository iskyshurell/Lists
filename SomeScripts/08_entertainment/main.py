import random

def throw(N, i):
	start = random.randint(0, N - 1)
	stop = random.randint(start, N - 1)

	print("Бросок", i + 1)
	print("Сбиты палки с номера", list[start], "по номер", list[stop])

	for i in list[start:stop + 1]:
		if downed.count(i) == 0:
			downed.append(i)

N = int(input("Кол-во палок: "))
K = int(input("Кол-во бросков: "))

list = [i for i in range(1, N + 1)]
downed = []


for i in range(K):
	throw(N, i)

print([("I" if downed.count(i_elem) == 0 else ".") for i_elem in list])
