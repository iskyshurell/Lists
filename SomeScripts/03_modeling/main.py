from abc import ABC, abstractmethod
import math




class TwoD_Figure(ABC):
    """ 2Д фигура - описываеться длиной"""
    @abstractmethod
    def __init__(self, lenght: float) -> None:
        self._lenght = lenght

    @property
    def lenght(self):
        return self.lenght

    @lenght.setter
    def lenght(self, lenght):
        self._lenght = lenght

class Square(TwoD_Figure):
    """Дочерний класс - Квадрат. Описываеться длиной и считает {площадь и периметр}"""
    def __init__(self, lenght: float) -> None:
        super().__init__(lenght)

    @property
    def P(self) -> float:
        return 4 * self._lenght

    @property
    def S(self) -> float:
        return self._lenght ** 2

class Triangle(TwoD_Figure):
    """Дочерний класс - Треугольник. Описываеться длиной и высотой, считает {площадь и периметр}"""
    def __init__(self, lenght: float, height: float) -> None:
        super().__init__(lenght)
        self._height = height

    @property
    def P(self) -> float:
        return 2 * math.sqrt(self._height ** 2 + (self._lenght / 2) ** 2) + self._lenght

    @property
    def S(self) -> float:
        return (self._lenght * self._height / 2)

    @property
    def height(self):
        return self.height

    @height.setter
    def height(self, height):
        self._height = height



class CountS(ABC):
    """Класс примесь в котором реализованы геттеры площади и периметра и так же подсчёт площади поверхности 3Д фигуры"""
    def count(self) -> float:
        return len(self._surface) * self._surface[0].S

    @property
    def P(self):
        return self._surface[0].P

    @property
    def S(self):
        return self._surface[0].S

    def lenght(self, lenght):
        for i in self._surface:
            i.lenght = lenght
class Cube(CountS):
    """3Д фигура - Квадрат, которая описана списком 2Д фигур. Дочерний класс от CountS"""
    def __init__(self, lenght: float) -> None:
        self._surface = []
        for i in range(6):
            self._surface.append(Square(lenght))

class Pyramid(CountS):
    """3Д фигура - Круг, которая описана списком 2Д фигур. Дочерний класс от CountS"""
    def __init__(self, lenght: float, height: float) -> None:
        self._surface = []
        for i in range(5):
            self._surface.append(Triangle(lenght, height))

    def height(self, value):
        for i in self._surface:
            i.hight = value


a = Cube(4.0)
print(a.count())
a.lenght(7.0)
print(a.count())
print(a.S, a.P)

print()
a = Pyramid(4.0, 5.0)
print(a.count())
print(a.S, a.P)

a.lenght(7.0)
a.height(9.0)
print(a.count())
print(a.S, a.P)