# Задание №2
# 📌 Создайте класс прямоугольник.
# 📌 Класс должен принимать длину и ширину при создании
# экземпляра.
# 📌 У класса должно быть два метода, возвращающие периметр
# и площадь.
# 📌 Если при создании экземпляра передаётся только одна
# сторона, считаем что у нас квадрат.


# Задание №5
# 📌 Дорабатываем класс прямоугольник из прошлого семинара.
# 📌 Добавьте возможность сложения и вычитания.
# 📌 При этом должен создаваться новый экземпляр
# прямоугольника.
# 📌 Складываем и вычитаем периметры, а не длинну и ширину.
# 📌 При вычитании не допускайте отрицательных значений.

class Rectangle:
    """Класс пряпоугольник с методами расчета площади, периметра, сложения и вычитания двух прямоугльниокв"""

    def __init__(self, side1: int, side2: int = None):
        """МЕтодо инициализации сторон прямоуглоьника"""
        self.side1 = side1
        self.side2 = side2 if side2 is not None else side1

    def area(self) -> int:
        """Метод расчета площади прямоугольника"""
        return self.side1 * self.side2

    def perimetr(self):
        """Метод расчета периметра прямоугольника"""
        return 2*(self.side1 + self.side2)

    def __add__(self, other):
        """Переопределенный метод сложения двух прямоугольников"""
        new_perimetr = self.perimetr() + other.perimetr()
        new_side1 = self.side1
        new_side2 = new_perimetr / 2 - new_side1
        return Rectangle(new_side1, new_side2)

    def __sub__(self, other):
        """Переопределенный метод вычитания двух прямоугольников"""
        new_perimetr = abs(self.perimetr() - other.perimetr())
        new_side1 = min([self.side1, self.side2, other.side1, other.side2])
        new_side2 = new_perimetr / 2 - new_side1
        return Rectangle(new_side1, new_side2)


if __name__ == '__main__':
    rect1 = Rectangle(2, 5)
    rect2 = Rectangle(5, 10)
    print(f'{rect1.area()=} {rect1.perimetr()=}')
    print(f'{rect2.area()=} {rect2.perimetr()=}')

    rec_sum = rect1 + rect2
    print(rec_sum.side1, rec_sum.side2)
    rec_sub = rect1 - rect2
    print(rec_sub.side1, rec_sub.side2)
