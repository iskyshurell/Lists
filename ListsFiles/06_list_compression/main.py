list = [0, 6, 5, 0, 3, 4, 0, 2]

for i_sym in list:
	if i_sym == 0:
		list.append(0)
		list.remove(0)

#Если не премещать нули можно сделать проще: new_l = [i_sym for i_sym in list if i_sym != 0]


list = list[:-list.count(0)]
print(list)