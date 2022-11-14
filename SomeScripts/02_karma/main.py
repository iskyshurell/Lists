import random
import os

def one_day(errors, file, day_count, error = ""):
	try:
		if random.randint(1, 10) == 1:
			error = random.choice(errors)
			raise error("Ошибка!")

	except:
		file.write(f"Ошибка! {error} - {day_count} день\n")

	finally:
		return random.randint(1, 7)





def main(carma = 0, day_count = 0, errors = ("KillError", "DrunkError",
                                             "CarCrashError", "GluttonyError",
                                             "DepressionError")):
	with open("karma.log", "w", encoding = "utf-8") as karma:

		while carma < 500:
			day_count += 1
			carma += one_day(errors, karma, day_count)

main()
