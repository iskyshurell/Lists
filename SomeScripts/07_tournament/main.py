import os
from operator import itemgetter



def first_tour(count = 0, new_list = []):
	print("Содержимое файла first_tour.txt: ")
	for i in open(file = "first_tour.txt"):
		if count == 0:
			K = i
		else:
			new_list.append(i[0:-1])
		count += 1
		print(i, end = "")

	return changing(K, new_list)

def changing(K, new_list):
	temp = [i_elem.split() for i_elem in new_list]
	return [i_elem for i_elem in temp if i_elem[-1] > K]

def second_tour(end_list, count = 1):
	print("\nСодержимое файла second_tour.txt:")
	file = open("second_tour.txt", "w")
	file.write(f"{len(end_list)}\n")

	sorted_list = sorting(end_list)

	for i in sorted_list:
		print(f"\n{count}) {i[1][0]}. {i[0]} {i[-1]}")
		file.write(f"\n{count}) {i[1][0]}. {i[0]} {i[-1]}")
		count += 1

	file.close()
	
def sorting(end_list):
	return sorted(end_list, key = itemgetter(2), reverse = True)

end_list = first_tour()
second_tour(end_list)


# import os
# from operator import itemgetter
# count = 0
# new_list = []
# print("Содержимое файла first_tour.txt: ")
#
# for i in open(file = "first_tour.txt"):
# 	if count == 0:
# 		K = i
# 	else:
# 		new_list.append(i[0:-1])
# 	count += 1
# 	print(i, end = "")
#
# temp = [i_elem.split() for i_elem in new_list]
# end_list = [i_elem for i_elem in temp if i_elem[-1] > K]
# print("\nСодержимое файла second_tour.txt:")
#
#
# count = 1
# file = open("second_tour.txt", "w")
# file.write(f"{len(end_list)}\n")
#
# sort_list = sorted(end_list, key = itemgetter(2), reverse = True)
#
# for i in sort_list:
# 	file.write(f"\n{count}) {i[1][0]}. {i[0]} {i[-1]}")
# 	count += 1
#
# file.close()