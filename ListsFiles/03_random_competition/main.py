import random

first = [round(random.random(), 2) + random.randint(5, 9) for _ in range(20)]
second = [round(random.random(), 2) + random.randint(5, 9) for _ in range(20)]
winners = [
	(second[i_elem] if second[i_elem] > first[i_elem] else first[i_elem])
           for i_elem in range(20)
			]
print("1-я команда:", first)
print("2-я команда:", second)
print("Победители:", winners)