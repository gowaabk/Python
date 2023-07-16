# Задание №1
# 📌 Напишите программу, которая использует модуль logging для
# вывода сообщения об ошибке в файл.
# 📌 Например отлавливаем ошибку деления на ноль.


import logging


logging.basicConfig(filename='python\dz15\error.log',
                    level=logging.ERROR, encoding='utf-8')


def division(a: int, b: int) -> float:
    try:
        return a / b
    except ZeroDivisionError as zd:
        logging.error(f' Ошибка {zd}')


if __name__ == "__main__":
    division(4, 0)
