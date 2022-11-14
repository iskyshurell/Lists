import os

def main(summ = 0):
	for i_string in open("numbers.txt"):
		new_string = temp_string(i_string)

		if len(new_string) > 0:

			summ = summ_count(summ, new_string)

	saving_result(summ)


def summ_count(summ, new_string):
	for i_elem in new_string:
		summ += int(i_elem)
	return summ

def temp_string(string):
	return [i_sym for i_sym in string if i_sym.isdigit()]



def saving_result(summ):
	temp = open("numbers.txt", "a")
	temp.write(f"\n {summ}\n")
	temp.close()


main()

#зачет


# for temp in open("numbers.txt"):
# 	for i_sym in temp:
# 		if flag:
# 			if i_sym.isdigit():
# 				new_sym += str(i_sym)
# 				flag = True
# 			else:
# 				summ += int(new_sym)
#
# 				new_sym = ""
# 				flag = False
#
# 		elif i_sym.isdigit():
# 			new_sym += str(i_sym)
# 			flag = True







