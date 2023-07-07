# Задание №1
# 📌 Создайте класс-функцию, который считает факториал числа при
# вызове экземпляра.
# 📌 Экземпляр должен запоминать последние k значений.
# 📌 Параметр k передаётся при создании экземпляра.
# 📌 Добавьте метод для просмотра ранее вызываемых значений и
# их факториалов.


import json
from typing import Any


class Fact():

    _context_dict = dict()

    def __init__(self, k: int):
        self.k = k
        self.save_list = list()

    def __call__(self, value):
        res = 1
        for i in range(2, value + 1):
            res *= i
            self.save_list.append(res)
            if len(self.save_list) > self.k:
                self.save_list.pop(0)
        return self.save_list[-1]

    def __str__(self) -> str:
        return f'{self.save_list}'

# Задание №2
# 📌 Доработаем задачу 1.
# 📌 Создайте менеджер контекста, который при выходе
# сохраняет значения в JSON файл.

    def mapper(self):
        for i, value in enumerate(self.save_list, start=1):
            self._context_dict[i] = value

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.mapper()
        with open('json.json', "w") as f:
            json.dump(self._context_dict, f, indent=2)


if __name__ == "__main__":

    with Fact(5) as fact:
        # fact = Fact(5)
        print(fact(2))
        print(fact(3))
        print(fact(4))
        print(fact(5))
        print(fact(6))
        print(fact(7))
        print(fact(8))
        print(fact)
