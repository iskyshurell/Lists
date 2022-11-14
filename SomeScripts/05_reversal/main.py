
text = input("Введите строку: ")
text = list(text)
temp = text[:]

start = temp.index("h")

for _ in range(temp.count("h") - 1):
	temp.remove("h")

stop = temp.index("h") + text.count("h") - 1

reverse = text[start + 1:stop]

print(reverse[::-1])