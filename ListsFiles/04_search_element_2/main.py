site = {
	'html': {
		'head': {
			'title': 'Мой сайт'
		},
		'body': {
			'h2': 'Здесь будет мой заголовок',
			'div': 'Тут, наверное, какой-то блок',
			'p': 'А вот здесь новый абзац'
		}
	}
}


key = input("Какой ключ ищем? ")
deep = int(input("Введите глубину (по умолчанию -1): "))


def finding_key(dictionary = site, my_key = key, my_deep = deep):
	if my_deep != 0:
		if my_key in dictionary:
			return dictionary[my_key]

		for i in dictionary.values():
			if isinstance(i, dict):
				result = finding_key(dictionary = i, my_deep = my_deep - 1)
				if result:
					break
		else:
			result = None

		return result
	else:
		return "На этой глубине ключ не найдено"

print(finding_key())