from math import pi

class MyMath:

    def __init__(self, lenght):
        self._lenght = lenght

    def circle_len(self) -> int:
        return 2 * pi * self._lenght

    def circle_sq(self):
        return pi * self._lenght ** 2

    def cube_S(self):
        return self._lenght ** 3

    def sphere_sq(self):
        return 4 * pi * self._lenght ** 2

res_1 = MyMath(5).circle_len()
res_2 = MyMath(6).circle_sq()
print(res_1)
print(res_2)