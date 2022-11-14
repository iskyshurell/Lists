import os
import zipfile
from operator import itemgetter




def txt_exists():
	if not os.path.exists("voyna-i-mir.txt"):
		zipfile.ZipFile("voyna-i-mir.zip").extract("voyna-i-mir.txt")

def main(sym_count = 0, sym_dict = {}):
	for i_str in open("voyna-i-mir.txt", encoding = "utf-8"):
		for i_sym in i_str:
			temp = count_sym(i_sym, sym_count, sym_dict)
			sym_count = temp[0]
			sym_dict = temp[1]

	return (sym_count, sym_dict)

def count_sym(sym, sym_count, sym_dict):
	if sym.isalpha():
		sym_count += 1
		if sym in sym_dict:
			sym_dict[sym] += 1
		else:
			sym_dict[sym] = 1

	return (sym_count, sym_dict)

def sorted_dict(sym_dict, new_list = []):
	for i_key, i_value in sym_dict.items():
		new_list.append((i_key, i_value))
	return sorted_by_nums(new_list)
	


def sorted_by_nums(new_list):
	return sorted(new_list, key = itemgetter(1))


def saving_result(sorted_list, sym_count):

	result = open("result.txt", "w")

	for i_elem in sorted_list:
		result.write(f"{i_elem[0]} - {i_elem[1]} \n")

	result.write(f"Всего букв: {sym_count}")
	result.close()


txt_exists()

temp = main()
sym_count = temp[0]
sym_dict = temp[1]

sorted_list = sorted_dict(sym_dict)
saving_result(sorted_list, sym_count)







# for i_str in open("voyna-i-mir.txt", encoding = "utf-8"):
# 	for i_sym in i_str:
# 		if i_sym.isalpha():
# 			sym_count += 1
# 			if i_sym in sym_dict:
# 				sym_dict[i_sym] += 1
#
# 			else:
# 				sym_dict[i_sym] = 1
#
# for i_key, i_value in sym_dict.items():
# 	new_list.append((i_key, i_value))
#
# sorted_list = sorted(new_list, key = itemgetter(1))
#
# print(sorted_list)
# result = open("result.txt", "w")
#
# for i_elem in sorted_list:
# 	result.write(f"{i_elem[0]} - {i_elem[1]} \n")
# result.write(f"Всего букв: {sym_count}")
# result.close()
