from typing import Callable



def debuger(func: Callable) -> Callable:
    def wrapper(*args: str, **kwargs: int) -> None:
        print(f"Название функции: {func.__name__}")

        kwargs_l = [f"{i_key}={i_value}" for i_key, i_value in kwargs.items()]
        print(f"Передаваемые аргументы: {','.join(args)},{','.join(kwargs_l)}")
        result = func(*args, **kwargs)
        print(f"Функция возвращает: {result}\n")

    return wrapper




@debuger
def greeting(name, age=None):
    if age:
        return "Ого, {name}! Тебе уже {age} лет, ты быстро растешь!".format(name=name, age=age)
    else:
        return "Привет, {name}!".format(name=name)

greeting("Том")
greeting("Миша", age=100)
greeting(name="Катя", age=16)
