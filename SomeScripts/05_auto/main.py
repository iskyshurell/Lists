import math


'''
Класс Car():
	__init__ - инициализация координат и угла
	
	move() - движение обьекта по оси координат,
			 принимает дистанцию движения
			
	change_angle() - изменяет угол движения(направление)

	cords_getter() - выводит информацию о координатах
	
Класс Bus():
	exit(), come_in() - методы для изменения числа пасажиров
	
	move() - теперь не только реализовывает движение но и считает количество денег
			по формуле: кол-во пассажиров * руб\км * км

	cords_getter() - выводит всю информацию о автобусе

def main(): - метод для проверки всех функций класса Car и его наследника Bus

'''

class Car():
	def __init__(self, x, y, angle):
		self.__x = x
		self.__y = y
		self.__angle = round(math.radians(angle), 3)

	def move(self, distance):
		self.__x = round(distance * math.cos(self.__angle), 3)
		self.__y = round(distance * math.sin(self.__angle), 3)

	def change_angle(self):
		self.__angle = round(math.radians(int(input("Введите угол в градусах: "))), 3)

	def cords_getter(self):
		return f"x = {self.__x}, y = {self.__y}"

class Bus(Car):
	def __init__(self, x = 0, y = 0, angle = 0, people = 0, salary = 0):
		super().__init__(x, y, angle)

		self.__people = people
		self.__salary = salary

	def come_in(self):
		__quantity = int(input("Сколько пассажиров войдёт? "))
		self.__people += __quantity

	def exit(self):
		__quantity = int(input("Сколько пассажиров выйдет? "))
		self.__people -= __quantity

	def move(self, distance, cost):
		super().move(distance)
		self.__salary += (cost * distance * self.__people)

	def cords_getter(self):
		cords = super().cords_getter()
		return f"Координаты: {cords}\nПассажиров - {self.__people}, Денег - {self.__salary}\n"



def main():
	bus = Bus()

	cost = int(input("Введите тариф поездки (руб\км): "))
	print()

	while True:
		distance = int(input("Введите дистанцию: (км) "))
		print()
		flag = input("Изменить направление движения? (True) ")
		print()
		if flag.lower() == "true":
			bus.change_angle()

		flag = input("Люди входят, выходят? (True, False, None) ")
		print()


		if flag.lower() == "true":
			bus.come_in()
		elif flag.lower() == "false":
			bus.exit()


		bus.move(distance, cost)
		print(bus.cords_getter())

main()


