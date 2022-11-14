# def calculating_math_func(data):
#     result = 1
#     for index in range(1, data + 1):
#         result *= index
#     result /= data ** 3
#     result = result ** 10
#     return result

num = int(input("Введите желаемое число: "))
factorials = {1:1}

def math_func(data, factorials, count = 1):
    if count != data:
       factorials[count + 1] = factorials[count] * (count + 1)
       return math_func(num, factorials, count = count + 1)
    result = (factorials[data] / (data ** 3)) ** 10
    return result



print(math_func(num, factorials))
print(factorials)