import os

def gen_files_path(searching, dir = os.path.abspath(os.sep)):
	for i_dir in os.listdir(dir):
		yield dir + i_dir
		if str(i_dir) == str(searching):
			return False
			

	
def main():
	searching_dir = input("Введите дирректорию: ")
	searching_folder = input("Введите каталог: ")

	if searching_dir.startswith(os.path.abspath(os.sep)):
		for i in gen_files_path(searching_folder, searching_dir):
			print(i)
	else:
		for i in gen_files_path(searching_folder):
			if i:
				print(i)

main()



