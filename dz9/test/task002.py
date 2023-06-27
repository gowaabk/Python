# Задание №2
# 📌 Дорабатываем задачу 1.
# 📌 Превратите внешнюю функцию в декоратор.
# 📌 Он должен проверять входят ли переданные в функцию-
# угадайку числа в диапазоны [1, 100] и [1, 10].
# 📌 Если не входят, вызывать функцию со случайными числами
# из диапазонов.

import random
from typing import Callable


def deco(func: Callable):
    MIN_COUNT = 1
    MAX_COUNT = 10
    MIN_NUM = 1
    MAX_NUM = 100

    def wrapper(*args, **kwargs):
        input_count, input_num = args
        if MIN_COUNT > input_count or input_count > MAX_COUNT:
            input_count = random.randint(MIN_COUNT, MAX_COUNT)
        if MIN_NUM > input_num or input_num > MAX_NUM:
            input_num = random.randint(MIN_NUM, MAX_NUM)
        return func(input_count, input_num)
    return wrapper


@deco
def two_numbers(count: int, num: int) -> Callable[[], None]:
    def random_numbers():
        for i in range(1, count+1):
            user_input = int(
                input("Введите задуманное число от 1 до 100 : -> "))
            if user_input == num:
                print(f"ВЫ угадали с {i} раза")
                break
        else:
            print("Вы не угадали")
    return random_numbers


# two_numbers(3, 20)()
# sd = two_numbers(3, 20)()
sd = two_numbers(11, 20)
sd()
