## Задача 4. Дебаг
Напишите декоратор debug, который при каждом вызове декорируемой функции выводит её имя (вместе со всеми передаваемыми аргументами) и затем какое значение она возвращает. И после этого выводится результат её выполнения

####Пример декорируемой функции:
````python
def greeting(name, age=None):
    if age:
        return "Ого, {name}! Тебе уже {age} лет, ты быстро растешь!".format(name=name, age=age)
    else:
        return "Привет, {name}!"~~.format(name=name)~~
````

####Основной код:
````python
greeting("Том")
greeting("Миша", age=100)
greeting(name="Катя", age=16)
````

####Результат:
````
Вызывается greeting("Том")
'greeting' вернула значение 'Привет, Том!'
Привет, Том!

Вызывается greeting("Миша", age=100)
'greeting' вернула значение 'Ого, Миша! Тебе уже 100 лет, ты быстро растешь!'
Ого, Миша! Тебе уже 100 лет, ты вырос!

Вызывается greeting(name="Катя", age=16)
'greeting' вернула значение 'Ого, Катя! Тебе уже 16 лет, ты быстро растешь!'
Ого, Катя! Тебе уже 16 лет, ты быстро растешь!
````


