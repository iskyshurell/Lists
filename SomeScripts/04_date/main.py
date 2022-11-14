from typing import Callable


class Date:

	def from_string(sel,  str_date: str = None) -> str:
		__list_date = str_date.split("-")
		return f"День - {__list_date[0]} Месяц - {__list_date[1]} Год - {__list_date[2]}"

	def is_valid(self, str_date: str = None) -> bool:
		__list_date = str_date.split("-")
		if (int(__list_date[0]) in range(1, 32))\
				and (int(__list_date[1]) in range(1, 13))\
					and (int(__list_date[-1]) * -1 < int(__list_date[-1])):
			return True
		return False

date = Date().from_string('10-12-2077')
print(date)
print(Date().is_valid('10-12-2077'))
print(Date().is_valid('40-12-2077'))
