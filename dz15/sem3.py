# Задание №3
# 📌 Доработаем задачу 2.
# 📌 Сохраняйте в лог файл раздельно:
# ○ уровень логирования,
# ○ дату события,
# ○ имя функции (не декоратора),
# ○ аргументы вызова,
# ○ результат.

import logging
from typing import Callable


FORMAT = "{levelname} - {asctime} : {msg}"
logging.basicConfig(format=FORMAT, style='{', filename='python\dz15\sem3.log',
                    level=logging.INFO, encoding='utf-8')

logger = logging.getLogger(__name__)


def deco_logger(func: Callable):
    def wrapper(*args, **kwargs):
        a, b = args
        res = func(a, b)
        logger.info(f" {func.__name__} {a} * {b} =  {res}")
    return wrapper


@deco_logger
def mult(a: int, b: int, *args, **kwargs) -> int:
    return a * b


if __name__ == "__main__":

    mult(4, 5)
