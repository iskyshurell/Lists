class Stack():
	def __init__(self):
		self.__st = []

	def __str__(self):
		return str(self.__st)

	def append_e(self, object):
		flag = False
		elem = ""

		for i in self.__st:
			if object in i:
				elem = i
				flag = True
				break

		if flag:
			index = self.__st.index(elem)
			if not isinstance(self.__st[index], dict):
				self.__st[index] = dict()
				self.__st[index][object] = 1

			self.__st[index][object] += 1

		else:
			self.__st.append(object)

	def pop(self):
		if len(self.__st) > 0:
			self.__st.pop()

	def remove(self, elem):
		flag = False
		index = 0

		for i_elem in self.__st:
			if elem in i_elem:
				index = self.__st.index(i_elem)
				flag = True
				break

		if flag and isinstance(self.__st[index], dict):
			self.__st[index][elem] -= 1


class TaskManager():
	def __init__(self):
		self.__dict = dict()

	def __str__(self):
		new_list = []
		for i_elem in sorted(self.__dict.keys()):
			new_list.append(f"{i_elem} {self.__dict[i_elem]}\n")

		return "".join(new_list)

	def remove_elem(self, object, priority):
		self.__dict[priority].remove(object)


	def new_elem(self, elem, priority):
		if priority not in self.__dict:
			self.__dict[priority] = Stack()
		self.__dict[priority].append_e(elem)

manager = TaskManager()
manager.new_elem("сделать уборку", 4)
manager.new_elem("помыть посуду", 4)
manager.new_elem("отдохнуть", 1)
manager.new_elem("поесть", 2)
manager.new_elem("сдать дз", 2)
manager.new_elem("сдать дз", 2)
manager.new_elem("сдать дз", 2)

print(manager)
manager.remove_elem("сдать дз", 2)
manager.remove_elem("сдать дз", 2)
print(manager)
