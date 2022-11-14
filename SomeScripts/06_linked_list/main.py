from typing import Any, Optional


class Info:
	def __init__(self, value: Optional[None] = None, next: Optional['Info'] = None) -> None:
		self.value = value
		self.next = next

	def __str__(self) -> str:
		return f"Узел: {self.value}"

class LinkedList:
	def __init__(self, head: Optional['Info'] = None) -> None:
		self.head = head
		self.lenght = 0

	def append(self , elem) -> None:
		new_elem = Info(elem)
		if self.head is None:
			self.head = new_elem
			self.lenght += 1
			return

		last_elem = self.head
		while last_elem.next:
			last_elem = last_elem.next
		last_elem.next = new_elem
		self.lenght += 1

	def remove(self, to_remove):
		temp = self.head
		index = 0
		
		if self.lenght == 0 or self.lenght <= to_remove:
			raise IndexError
		else:
			if not temp is None:
				if to_remove == 0:
					self.head = temp.next
					self.lenght -= 1
					return
			while not temp is None:
				if to_remove == index:
					break
				prev = temp
				temp = temp.next
				index += 1
			prev.next = temp.next
			self.lenght -= 1

	def get(self, to_get):
		temp = self.head
		if self.lenght == 0 or self.lenght <= to_get:
			raise IndexError

		for i in range(to_get):
			temp = temp.next

		return temp.value
		


	def iter(self) -> str:
		last_elem = self.head
		yield last_elem
		while last_elem.next:
			last_elem = last_elem.next
			yield last_elem

my_list = LinkedList()
my_list.append("GG")
my_list.append(50)
my_list.append(60)
my_list.remove(2)



for i in my_list.iter():             #Вывод информации
	print(i)

print(my_list.get(1))          #Получение второго элемента



