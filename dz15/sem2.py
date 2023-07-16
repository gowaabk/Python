# Задание №2
# 📌 На семинаре про декораторы был создан логирующий
# декоратор. Он сохранял аргументы функции и результат её
# работы в файл.
# 📌 Напишите аналогичный декоратор, но внутри используйте
# модуль logging.


import logging
from typing import Callable


logging.basicConfig(filename='python\dz15\info.log',
                    level=logging.INFO, encoding='utf-8')

logger = logging.getLogger(__name__)


def deco_logger(func: Callable):
    def wrapper(*args, **kwargs):
        a, b = args
        res = func(a, b)
        logger.info(f" {a} * {b} =  {res}")
    return wrapper

# def deco(func: Callable):
#     final_dict = {}
#     with open(f'{func.__name__}.json', 'r') as f:
#         data = json.load(f)
#         final_dict.update(data)

#     def wrapper(*args, **kwargs):
#         res = func(*args, **kwargs)
#         for i in range(len(args)):
#             final_dict.update({str(i): args[i]})
#         final_dict.update(**kwargs)
#         with open(f'{func.__name__}.json', 'w') as f:
#             json.dump(final_dict, f, indent=2)

#     return wrapper


@deco_logger
def mult(a: int, b: int, *args, **kwargs) -> int:
    return a * b


if __name__ == "__main__":

    mult(4, 5)
