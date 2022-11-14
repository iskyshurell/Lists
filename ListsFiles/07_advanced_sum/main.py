my_list = ([[1, 2, [3]], [1], 3])
# my_list = (1, 2, 3, 4, 5)
sum = 0
def summ(sum, num = my_list):
	for i_num in num:
		if isinstance(i_num, list):
			sum = summ(sum, num = i_num)
		else:
			sum += i_num
	return sum

print(f"Ответ: {summ(sum)}")
