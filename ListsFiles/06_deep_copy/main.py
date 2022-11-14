site = {
    'html': {
        'head': {
            'title': 'Куплю/продам iphone недорого'
        },
        'body': {
            'h2': 'У нас самая низкая цена на iphone',
            'div': 'Купить',
            'p': 'продать'
        }
    }
}
word = ""

N = int(input("Сколько сайтов? "))


def key_in_dict(my_dict):
	for i in my_dict.keys():
		if i in my_dict:
			return True
	return False

def copy(my_word = word, new = site):
	new_site = {}
	for key, value in new.items():
		if isinstance(value, dict):
			if key_in_dict(new_site):
				new_site[key] = copy(my_word = word, new = value)
			else:
				new_site = {key:copy(my_word = word, new = value)}
		else:
			if "iphone" in value:
				value = value.replace("iphone", my_word)
			if key_in_dict(new_site):
				new_site[key] = value
			else:
				new_site = {key:value}

	return new_site





for _ in range(N):
	word = input("Введите название продуктва для нового сайта: ")

	print(f"Сайт для {word}: \n {copy(my_word = word)}")


