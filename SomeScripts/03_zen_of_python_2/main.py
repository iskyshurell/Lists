

def main(main_list = [0, 0],
		dictionary = {}):

	for i_str in open("zen.txt"):
		main_list[0] += 1
		main_list = word_count(i_str, main_list)
		for i_elem in i_str:
			if i_elem.isalpha():
				dictionary = count_sym(i_elem, dictionary)
	key = rarest_sym(dictionary)
	main_list.append(f"{key} - {dictionary[key]}")

	save_result(main_list)

def word_count(str, main_list):
	new_str = str.split()
	main_list[1] += len(new_str)
	return main_list


def count_sym(elem, dictionary):
	if elem.lower() in dictionary:
		dictionary[elem.lower()] += 1
	else:
		dictionary[elem.lower()] = 1

	return dictionary
		
def rarest_sym(dictionary):
	minn = -1
	for i_key, i_value in dictionary.items():
		if i_value <= minn or minn == -1:
			min_key = i_key
			minn = i_value
	return min_key

def save_result(main_list):
	file = open("result.txt", "w")
	for i_elem in main_list:
		file.write(f"{str(i_elem)}\n")
	file.close()

main()


# zen = []
# words = []
# s_dict = dict()
# str_count = 0
# word_count = 0
# sym_count = 0
# minn = -1
#
# for i_string in open("zen.txt", "r"):
# 	str_count += 1
# 	i_str = str(i_string).split()
# 	for i_word in i_str:
# 		words.append(i_word)
# 	word_count += len(i_str)
#
#
# for i_word in words:
# 	for i_sym in i_word:
# 		sym_count += 1
# 		if i_sym.lower() in s_dict and i_sym.isalpha():
# 			s_dict[i_sym.lower()] += 1
# 		elif i_sym.isalpha():
# 			s_dict[i_sym.lower()] = 1
#
# for i_key, i_value in s_dict.items():
# 	if i_value <= minn or minn == -1:
# 		min_int = f"Самый редкий символ: {i_key} - {i_value}"
# 		minn = i_value
#
# print(f"Строк - {str_count}, Слов - {word_count}")
# print(min_int)
