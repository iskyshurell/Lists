end_num = int(input("Введите длину списка: "))

numbers = [(1 if i_num % 2 == 0 else i_num % 5) for i_num in range(end_num)]
print("Результат:", numbers)
