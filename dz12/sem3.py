# Задание №4
# 📌 Доработайте класс прямоугольник из прошлых семинаров.
# 📌 Добавьте возможность изменять длину и ширину
# прямоугольника и встройте контроль недопустимых значений
# (отрицательных).
# 📌 Используйте декораторы свойств

class Rectangle:
    def __init__(self, side1: int, side2: int = None):
        self._side1 = side1
        self._side2 = side2 if side2 is not None else side1

    @property
    def side1(self):
        return self._side1
    
    @property
    def side2(self):
        return self._side2
    
    @side1.setter
    def side1(self, value):
        if value > 0:
            self._side1 = value
        else:
            raise ValueError(f'{value} не может быть отрицательным')

    @side2.setter
    def side2(self, value):
        if value > 0:
            self._side2 = value
        else:
            raise ValueError(f'{value} не может быть отрицательным')

    def area(self) -> int:
        return self.side1 * self.side2

    def perimetr(self):
        return 2*(self.side1 + self.side2)


if __name__ == '__main__':
    rect1 = Rectangle(5, 10)
    print(rect1.side1, rect1.side2)
    rect1.side1 = 7
    rect1.side2 = 3
    print(rect1.side1, rect1.side2)

    rect1.side1 = -7
    # rect1.side2 = -3
    # print(rect1.side1, rect1.side2)
    # rect2 = Rectangle(5)
    # print(f'{rect1.area()=} {rect1.perimetr()=}')
    # print(f'{rect2.area()=} {rect2.perimetr()=}')
