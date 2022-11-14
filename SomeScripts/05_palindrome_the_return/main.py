from collections import Counter

if __name__ == '__main__':
	def sym_list(string: str) -> Counter:
		my_list = Counter()
		for i in list(string):
			my_list[i] += 1
		return my_list
	def check_for_poly(elem: Counter) -> bool:
		new_list = list(filter(lambda n: elem[n] % 2 != 0, elem))
		if len(new_list) > 1:
			return False
		return True

	def can_be_poly(word: str) -> bool:
		counter = sym_list(word)
		return check_for_poly(counter)
		
	print(can_be_poly('ababc'))
	print(can_be_poly('abbbc'))
