from userexception import *  # userMinLengthError, MyTriangleError, CheckBagSize


class Triangle:

    def __init__(self, a: int, b: int, c: int) -> None:
        if a > 0:
            self.a = a
        else:
            raise UserMinLengthError(a, 0)
        if b > 0:
            self.b = b
        else:
            raise UserMinLengthError(b, 0)
        if c > 0:
            self.c = c
        else:
            raise UserMinLengthError(c, 0)

    def check_sides(self):

        check1 = self.a + self.b
        check2 = self.a + self.c
        check3 = self.b + self.c
        if (check1 < self.c or check2 < self.b or check3 < self.a):
            raise UserTriangleError(self.a, self.b, self.c)
        else:
            if (a == b and b == c and c == a):
                print("Треугольник равносторонний")
            elif (a == b or b == c or c == a):
                print("Треугольник равнобедренный")
            else:
                print("Треугольник разносторонний")


class Bag:

    def __init__(self, bag: int, items: dict) -> None:
        self.bag = bag
        self.items = items

    def check_item(self):
        for elements in self.items:
            if self.bag < self.items[elements]:
                raise CheckBagSize(self.bag, self.items[elements])
            else:
                print(f"Предмет {elements} влезет в сумку")
        print("Предметы проверены")

    def pack_bag(self):
        result = []
        for elements in self.items:
            if self.bag > self.items[elements]:
                result.append(elements)
                self.bag = self.bag - int(self.items[elements])
            else:
                break
        return result


if __name__ == "__main__":
    TEXT = f"Введите длину стороны треугольника "
    try:
        a = int(input(TEXT + "A: "))
        b = int(input(TEXT + "B: "))
        c = int(input(TEXT + "C: "))
    except ValueError as v:
        print(f"Нужно задать число: {v}")

    t1 = Triangle(a, b, c)
    t1.check_sides()

    items = {'сапоги': 50,
             'Дождевик': 50,
             'БП': 100,
             'Спички': 10,
             'Палатка': 3000,
             'Мешок': 200,
             }
    bag = 1000

    b1 = Bag(bag, items)
    b1.check_item()
    print(b1.pack_bag())
