string = "abcdd"
tuple = (1, 2, 3, 4)
new_zip = []


def my_zip(str = string, tpl = tuple, count = 0, rec_count = min(len(string), len(tuple)) - 1):
	new_zip.append((str[count], tpl[count]))
	if count != rec_count:
		return my_zip(count = count + 1)


my_zip()
print(new_zip)


