num_pos = int(input("Введите позицию в ряде Фибоначчи: "))
row = [1, 0]

def num_count(count = num_pos):
	if count > 0:
		row.append(row[0] + row[1])
		row.remove(row[0])
		return num_count(count = count - 1)

num_count()
print(row[1])
