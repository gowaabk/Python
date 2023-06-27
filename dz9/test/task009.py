# Напишите следующие функции:
#     Нахождение корней квадратного уравнения <br>
#     Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.<br>
#     Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла.<br>
#     Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл.<br>


import csv
from math import sqrt
import random
import json
from typing import Callable


PATH_CSV = ".\\Python\\dz9\\test\\ABC.csv"
PATH_JSON = ".\\Python\\dz9\\test\\ABC.json"
min_row = 1  # Минимальное количество строк в csv
max_row = 10  # Максимальное количество строк в csv
# Границы рандомного числа
min_num = -100
max_num = 100

# создаем и заполняем csv
def gen_csv(min_row: int, max_row: int, min_num: int, max_num: int):
    with open(PATH_CSV, "w", encoding="UTF-8") as f:
        writer = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)
        for row in range(random.randint(min_row, max_row)):
            writer.writerow([random.randint(min_num, max_num), random.randint(min_num, max_num),
                             random.randint(min_num, max_num)])


def deco(func: Callable):
    gen_csv(min_row, max_row, min_num, max_num)

    def wrapper():
        with open(PATH_CSV, "r", encoding="UTF-8") as f:
            data = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
            for num in data:
                if num and num[0] != 0:
                    func(*num)
    return wrapper

# Формируем json с результатами вычислений

def create_json(func: Callable):
    res = []

    def wrapper(*args):
        roots = func(*args)
        new_dict = {"a": args[0], "b": args[1], "c": args[2], "roots": roots}
        res.append(new_dict)
        with open(PATH_JSON, 'w', encoding='UTF-8') as file:
            json.dump(res, file, indent=4)
        return roots
    return wrapper


@deco
@create_json
# Решение квадратного уравнения
def get_roots(*args):
    a, b, c = args
    # print(a, b, c)
    discr = b * b - 4 * a * c
    # print(discr)
    if discr > 0:
        x1 = (-b + sqrt(discr)) / (2 * a)
        x2 = (-b - sqrt(discr)) / (2 * a)
        return str(x1), str(x2)
    elif discr == 0:
        x = -b / (2 * a)
        return str(x)
    else:
        return None


# data = get_roots(1, 1, 1)
# print(data)

