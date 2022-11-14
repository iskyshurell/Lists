import os




file = open("text.txt", "r")

def fill(elem, count, alphabet):
	if elem.islower():
		if alphabet.index(elem) + count <= len(alphabet) - 1:
			return alphabet[alphabet.index(elem) + count]
		else:
			return alphabet[alphabet.index(elem) + count - len(alphabet)]
	else:
		if alphabet.index(elem.lower()) + count <= len(alphabet):
			return alphabet[alphabet.index(elem.lower()) + count].upper()
		else:
			return alphabet[alphabet.index(elem.lower()) + count - len(alphabet)].upper()


def main(file, count = 0, new_list = [],
         alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                     "u", "v", "w", "x", "y", "z"]):
	for i_string in file:
		count += 1
		i_string = changing_string(i_string)
		new_word = [fill(i_elem, count, alphabet)
		            for i_elem in i_string]
		new_list.append(new_word)

	return ["".join(i_elem) for i_elem in new_list]

def changing_string(i_string):
	i_string = [i_elem for i_elem in i_string if i_elem != "\n"]
	return "".join(i_string)

def saving(end_list):

	file = open("cipher_text.txt", "w")
	for i in end_list:
		file.write(f"{i}\n")
	file.close()

end_list = main(file)
saving(end_list)






