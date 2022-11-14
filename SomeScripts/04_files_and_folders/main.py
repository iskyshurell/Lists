import os

way = "F:\Dir"  #Тут путь

def dir_func(way, info = [0, 0, 0]):
	a = os.listdir(way)
	for i_directory in a:
		directory = path_creating(way, i_directory)
		
		info = main_action(directory, info)

	return info[::]

def path_creating(way, i_directory):
	return os.path.join("/", way, i_directory)

def main_action(directory, info):
	if os.path.isdir(directory):
		info[0] += 1
		dir_func(directory)
	else:
		info[1] += 1
		info[2] += os.path.getsize(directory)

	return info

info = dir_func(way)



print(f"{info[0]} - количество подкаталогов ")
print(f"Количество файлов: {info[1]}")
print(f"Размер каталога: {info[2] / 1024} Кб")

# files = 0
# size = 0
#
# def dir_func(way, dir_count = 0):
# 	global files, size
# 	a = os.listdir(way)
# 	for i_directory in a:
# 		directory = os.path.join("/", way, i_directory)
# 		if os.path.isdir(directory):
# 			dir_count += 1
# 			dir_count = dir_func(directory, dir_count = dir_count)
# 		else:
# 			files += 1
# 			size += os.path.getsize(directory)
#
# 	return dir_count
#
# dirs = dir_func(way)
# print(f"{dirs} - количество подкаталогов ")
# print(f"Количество файлов: {files}")
# print(f"Размер каталога: {size / 1024} Кб")