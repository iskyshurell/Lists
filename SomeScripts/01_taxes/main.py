class Propety:

	def __init__(self, worth, percent = 1):
		self.__worth = worth
		self.__percent = percent
		self.__cost = self.count()

	def count(self):
		return self.__worth // self.__percent

	def __str__(self):
		return f"Налог на недвижимость: {self.__cost}"

	def cost_getter(self):
		return int(self.__cost)

class Apartament(Propety):

	def __init__(self, worth):
		super().__init__(worth, percent = 1000)

class Car(Propety):

	def __init__(self, worth):
		super().__init__(worth, percent = 200)

class CountryHouse(Propety):

	def __init__(self, worth):
		super().__init__(worth, percent = 500)

def main():
	try:
		user_money = int(input("Введите количество ваших денег: "))

		flat_c = int(input("Введите стоимость квартиры: "))
		apart = Apartament(flat_c)
		print(apart)

		car_c = int(input("Введите стоимость машины: "))
		car = Car(car_c)
		print(car)

		country_house_c = int(input("Введите стоимость дачи: "))
		country_house = CountryHouse(country_house_c)
		print(country_house)

		results(sum((country_house.cost_getter(), apart.cost_getter(), car.cost_getter())), user_money)

	except ValueError:
		print("Вы ввели одну из стоимостей неправильно!")

def results(taxes_sum, user_money):
	if user_money < taxes_sum:
		print(f"Вам не хватает денег!\n У вас {user_money}")

	print(f"Ваш налог составляет {taxes_sum}")

main()