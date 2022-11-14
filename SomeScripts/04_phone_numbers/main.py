import re
from typing import List

def check(nums: List[str]) -> None:
	for i_n in range(1, 4):
		text = nums[i_n - 1]
		status = re.match(r'[8, 9]\d{9}', text)
		if status:
			print(f"{i_n} номер: всё в порядке")
		else:
			print(f'{i_n} номер: не подходит')


if __name__ == '__main__':
	nums = ['9999999999', '999999-999', '99999x9999']
	check(nums)