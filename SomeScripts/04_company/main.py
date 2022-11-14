
class Person():
	def __init__(self, name, surname, age):
		self.__name = name
		self.__surname = surname
		self.__age = age

	def info_getter(self):
		return f"{self.__name} {self.__surname} -- {self.__age}"


class Employee(Person):
	__salary = 0

	def count_salary(self):
		return self.__salary

class Manager(Employee):
	def __init__(self, name, surname, age):
		super().__init__(name, surname, age)
		self.__salary = 13000

	def count_salary(self):
		return self.__salary


class Agent(Employee):
	def __init__(self, name, surname, age, income):
		super().__init__(name, surname, age)
		self.__income = income

	def count_salary(self):
		return 5000 + (self.__income / 100 * 5)


class Worker(Employee):

	def __init__(self, name, surname, age, time):
		super().__init__(name, surname, age)
		self.__time = time

	def count_salary(self):
		return 100 * self.__time


def main():
	f_m = Manager("Василий", "Петров", 25)
	print(f_m.count_salary())
	print(f_m.info_getter())

	print()
	s_m = Manager("Иван", "Михайлович", 20)
	print(s_m.count_salary())
	print(s_m.info_getter())

	print()
	t_m = Manager("Сергей", "Попов", 28)
	print(t_m.count_salary())
	print(t_m.info_getter())

	print()
	f_a = Agent("Александр", "Кузнецов", 24, 200000)
	print(f_a.count_salary())
	print(f_a.info_getter())

	print()
	s_a = Agent("Михаил", "Рожков", 29, 100000)
	print(s_a.count_salary())
	print(s_a.info_getter())

	print()
	t_a = Agent("Антон", "Шастун", 42, 300000)
	print(t_a.count_salary())
	print(t_a.info_getter())

	print()
	f_w = Worker("Владислав", "Стрелков", 23, 14)
	print(f_w.count_salary())
	print(f_w.info_getter())

	print()
	s_w = Worker("Олег", "Кузнецов", 53, 12)
	print(s_w.count_salary())
	print(s_w.info_getter())

	print()
	t_w = Worker("Адам", "Крылов", 29, 42)
	print(t_w.count_salary())
	print(t_w.info_getter())

main()
