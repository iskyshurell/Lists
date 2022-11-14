new_zen = []

def main():
	new_zen = new_zen_creating()
	
	temp = open("new_zen.txt", "w")
	for i_str in new_zen:
		temp.write(i_str)

	temp.close()

def new_zen_creating():
	for i_string in open("zen.txt", "r"):
		new_zen.insert(0, i_string)

	return new_zen

main()

#мой вариант
import os

def get_file_path(file_name):
    return os.path.abspath(os.path.join('.', file_name))

def get_lines(file_name):
    file_path = get_file_path(file_name)
    out = []
    with open(file_path, 'r') as input_file:
        out += input_file.readlines()[::-1]

    return out

def main(input_filename):
    for line in get_lines(input_filename):
        print(line.replace('\n', ''))


main('zen.txt')



# for i_string in open("zen.txt", "r"):
# 	new_zen.insert(0, i_string)

# for i_str in new_zen:
# 	temp = open("new_zen.txt", "a")
# 	temp.write(i_str)
# 	temp.close()
