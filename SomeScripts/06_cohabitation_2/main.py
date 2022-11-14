import random

'''
class House:
 -- геттеры и сеттеры для 4-х переменных
	нужны для их получения и изменения
	
 -- stats() - возвращает информацию о конкретном доме
		
class Human():
 -- pet_the_cat() - Гладить кота + 5 счастья - 10 сытости
 -- eat_food() - Есть + сытость (макс 30) - еда(макс 30)
 -- status() -возвращает информацию о себе
 
class Husband():
 -- play_games - Метод класа Муж + 20 счастья - 10 голода
 -- go_to_work - Метод класа Муж + 150 денег - 10 голода
 
сlass Wife():
 -- buy_clothes() - Метод класа Жена + 60 счастья - 350 денег - 10 голода
 -- clear_the_house() - Уборка дома - грязь - сытость  
 -- buy_food and buy_cat_food - Покупка еды	+ еда - деньги 

class Cat():
 -- eat_cat_food() - есть еду + сытость - еда для кота
 -- sleep() - спать - сытость
 -- tear_wallpaper() - драть обои 
 
def init_p(): - инициализация дома и людей

def main_cycle(): - главный цикл с действием

def life_check()/ def clear_check - проверка все-ли живы и проверка чистоты

def Husband_a()/ def Wife_a()/ def Cat_a(): - Главное действие класов 

'''


class House:

	def __init__(self):
		self.__money = 100
		self.__food = 50
		self.__cat_food = 30
		self.__clear = 0

	def food_setter(self, eated):
		self.__food -= eated

	def food_getter(self):
		return self.__food

	def cat_food_setter(self, eated):
		self.__cat_food -= eated

	def cat_food_getter(self):
		return self.__cat_food

	def money_setter(self, payed):
		self.__money -= payed

	def money_getter(self):
		return self.__money

	def clear_setter(self, value):
		self.__clear -= value

	def clear_getter(self):
		return self.__clear

	def stats(self):
		return f"В доме:\n{self.__money} денег\n{self.__food} еды\n{self.__cat_food} еды для кота\n{self.__clear} грязи\n"

class Human():

	def __init__(self, name, home):
		self.__name = name
		self.__hunger = 30
		self.__happiness = 100
		self.__home = home

	def pet_the_cat(self):
		self.happiness_setter(5)
		self.hunger_setter()

	def eat_food(self, eated):
		self.__hunger += eated
		self.__home.food_setter(eated)

	def happiness_setter(self, value):  # Погладить кота 5, поиграть(муж) 20, шуба(жена) 60
		self.__happiness += value

	def hunger_setter(self):
		self.__hunger -= 10

	def home_getter(self):
		return self.__home

	def hunger_getter(self):
		return self.__hunger

	def happiness_getter(self):
		return self.__happiness

	def stats(self):
		return f"{self.__name} - {self.__hunger} сытость - {self.__happiness} счастье"

class Husband(Human):

	def __init__(self, name, home):
		super().__init__(name, home)

	def play_games(self):
		super().happiness_setter(20)
		super().hunger_setter()

	def go_to_work(self):
		home = super().home_getter()
		home.money_setter(-150)
		super().hunger_setter()

class Wife(Human):

	def __init__(self, name, home):
		super().__init__(name, home)

	def buy_clothes(self):
		super().happiness_setter(60)
		home = super().home_getter()
		home.money_setter(350)
		super().hunger_setter()

	def buy_food(self, value):
		home = super().home_getter()
		home.money_setter(value)
		home.food_setter(-value)
		super().hunger_setter()

	def buy_cat_food(self, value):
		home = super().home_getter()
		home.money_setter(value)
		home.cat_food_setter(-value)
		super().hunger_setter()

	def clear_the_house(self, value):
		super().hunger_setter()
		home = super().home_getter()
		home.clear_setter(value)

class Cat:

	def __init__(self, name, home):
		self.__name = name
		self.__hunger = 30
		self.__home = home

	def eat_cat_food(self, eated):
		self.__hunger += eated * 2
		self.__home.cat_food_setter(eated)

	def sleep(self):
		self.__hunger -= 10

	def tear_wallpaper(self):
		self.__home.clear_setter(-5)
		self.__hunger -= 10

	def hunger_setter(self):
		self.__hunger -= 10

	def hunger_getter(self):
		return self.__hunger

	def stats(self):
		return f"{self.__name} - {self.__hunger}\n сытости"

def init_p():
	home = House()
	husband = Husband("Валерий", home)
	wife = Wife("Оля", home)
	cat = Cat("Котик", home)
	cat2 = Cat("Котик2", home)
	cat3 = Cat("Котик3", home)

	main_cycle(home, husband, wife, cat, cat2, cat3)

def main_cycle(home, husband, wife, cat, cat2, cat3):
	for i_day in range(1, 366):

		if clear_check(home):
			husband.happiness_setter(-10)
			wife.happiness_setter(-10)

		if life_check(husband, wife, cat):
			print("Кто-то умер")
			break

		print(f"{i_day} - день!")
		print(f"\nСостояние дома:\n{home.stats()}\n")
		print(f'Состояние мужа:\n{husband.stats()}\n')
		print(f"Состояние жены:\n{wife.stats()}\n")
		print(f"Состояние котиков:\n{cat.stats()}\n{cat2.stats()}\n{cat3.stats()}\n")

		Husband_action(husband, home)
		Wife_action(wife, home)
		Cat_a(cat, home)
		Cat_a(cat2, home)
		Cat_a(cat3, home)


def life_check(h, w, c):
	if h.hunger_getter() <= 0 or h.happiness_getter() < 10:
		return True

	elif w.hunger_getter() <= 0 or w.happiness_getter() < 10:
		return True

	elif c.hunger_getter() <= 0:
		return True

	else:
		return False

def clear_check(home):
	if home.clear_getter() > 90:
		return True
	return False

def Husband_action(husband, home):
	if husband.hunger_getter() < 30 and home.food_getter() > 0:
		eated = min(30, 50 - husband.hunger_getter())
		if not home.food_getter() >= eated:
			eated = home.food_getter()
		husband.eat_food(eated)
		print("\nМуж ест\n")


	elif husband.happiness_getter() < 50:
		husband.play_games()
		print("\nМуж играет\n")
	elif home.money_getter() < 500:
		husband.go_to_work()
		print("\nМуж работает\n")

	else:
		husband.pet_the_cat()
		print("\nМуж гладит кота\n")

def Wife_action(wife, home):
	if wife.hunger_getter() < 30 and home.food_getter() > 0:
		eated = min(30, 50 - wife.hunger_getter())
		if not home.food_getter() >= eated:
			eated = home.food_getter()
		wife.eat_food(eated)
		print("\nЖена ест\n")

	elif wife.happiness_getter() < 50 and home.money_getter() >= 350:
		wife.buy_clothes()
		print("\nЖена покупает шубу\n")

	elif home.clear_getter() > 50:
		value = 100 - home.clear_getter()
		wife.clear_the_house(value)
		print("\nЖена убирает дома\n")

	elif home.food_getter() < 50:
		food = 50 - home.food_getter()
		if home.money_getter() < food:
			food = home.money_getter()

		wife.buy_food(food)

		food = 50 - home.cat_food_getter()
		if home.money_getter() < food:
			food = home.money_getter()

		wife.buy_cat_food(food)
		print("\nЖена идёт в магазин\n")

	else:
		wife.pet_the_cat()
		print("\nЖена гладит кота\n")

def Cat_a(cat, home):

	r_num = random.randint(1, 2)
	if cat.hunger_getter() < 30 and home.cat_food_getter() > 0:
		eated = min(50 - cat.hunger_getter(), 10)
		if home.cat_food_getter() < eated:
			eated = home.cat_food_getter()
		cat.eat_cat_food(eated)
		print("\nКот ест\n")

	elif r_num == 1:
		cat.sleep()
		print("\nКот спит\n")
	else:
		cat.tear_wallpaper()
		print("\nКот пакостит\n")

init_p()
