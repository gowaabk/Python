# Возьмите любые 1-3 задачи из прошлых домашних заданий.
# Добавьте к ним логирование ошибок и полезной информации.
# Также реализуйте возможность запуска из командной строки с передачей параметров.


import argparse
import logging


FORMAT = '{levelname} - {asctime} : {msg}'
logging.basicConfig(level=logging.INFO, filename='python\dz15\dz15.log', encoding='utf-8',
                    format=FORMAT, style='{')
logger = logging.getLogger(__name__)


def num_systems(num: int, number_sys: int = 2) -> str:

    if number_sys < 0:
        logger.error(f'Система счисления {number_sys} не существует')
        return float('inf')
    num_log = num
    result = ""
    while num >= 1:
        try:
            res = num % number_sys
            match res:
                case 10: res = "A"
                case 11: res = "B"
                case 12: res = "C"
                case 13: res = "D"
                case 14: res = "E"
                case 15: res = "F"
            result += str(res)
            num = num // number_sys
        except ZeroDivisionError as zd:
            logger.error(f'Система счисления {number_sys} не существует')
            return float('inf')
    logger.info(f'{num_log} в {number_sys} системе счисления = {result}')
    return result[::-1]


def parser_func():
    parser = argparse.ArgumentParser(
        description='Получаем аргументы из строки в формате task.py 7 2')
    parser.add_argument('num', type=int, default=10)
    parser.add_argument('num_sys', type=int, default=10)

    args = parser.parse_args()
    print(args)
    return num_systems(args.num, args.num_sys)


if __name__ == '__main__':
    print(num_systems(8, 2))
    print(num_systems(255, 16))
    print(num_systems(10, 8))
    print(num_systems(56, 0))
    print(num_systems(23, -2))
    parser_func()
