import datetime
import functools
import time
import os
from typing import Callable



def log_methods(date: str = None) -> Callable:
    def dec_func(cls) -> 'cls':
        for i_method in dir(cls):
            if not i_method.startswith("__"):
                old_method = getattr(cls, i_method)
                new_method = decorator(old_method)
                setattr(cls, i_method, new_method)

        return cls
    return dec_func

def decorator(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapped(self):
        print(f"Запуск функции {func.__name__} >> {self.__class__}. Время и дата запуска: {datetime.datetime.now()}")
        a = time.time()
        func(self)
        b = time.time()
        print(f"Завершение функции {func.__name__}. Время работы функции: {b - a} секунд.")

    return wrapped

@log_methods(date = f"{datetime.datetime.now()}")
class A:
    def test_sum_1(self) -> int:
        print('Тут метод test sum 1')
        number = 100
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result
    def ss(self):
        pass


@log_methods(date = f"{datetime.datetime.now()}")
class B(A):
    def test_sum_1(self):
        super().test_sum_1()
        print("Тут метод test sum 1 у наследника")

    def test_sum_2(self):
        print("Тут метод test_sum_2 у наследника")
        number = 200
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result

my_obj = B()
my_obj.test_sum_1()
my_obj.test_sum_2()



