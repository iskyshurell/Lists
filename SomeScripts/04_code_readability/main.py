



if __name__ == '__main__':
	print(list(filter(lambda x: x <= 2 or False not in [True if x % n != 0 else False for n in range(2, x)], range(1, 1001))))



	def check_for_num(x):
		for i in range(2, x):
			if x % i != 0:
				pass
			else:
				return False
		return True

	nums = (x for x in range(1, 10001) if check_for_num(x))
	
	print(list(nums))

	#Для меня более читабельный вариант решения с помощью генератора