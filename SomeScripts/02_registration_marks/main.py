import re

def find_cars(text: str) -> str:
	cars = re.findall(r'\b\w\d{3}\w{2}\d{2,3}\b', text)
	return f"Список номеров частных автомобилей: {cars}"

def find_taxi(text: str) -> str:
	taxi = re.findall(r'\b\w{2}\d{3}\d{2,3}\b', text)
	return f"Список номеров такси: {taxi}"


if __name__ == '__main__':

	numbers = 'А578ВЕ777 ОР233787 К901МН666 СТ46599 СНИ2929П777 666АМР666'

	print(find_cars(numbers))
	print(find_taxi(numbers))

