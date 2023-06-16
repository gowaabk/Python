# В модуль с проверкой даты добавьте возможность запуска в терминале
#  с передачей даты на проверку.
from sys import argv
from datetime import datetime

__all__ = ['check_year', 'date_validator']


def _check_leap_year(date: str) -> bool:
    CHECK_NORMAL_1 = 4
    CHECK_NORMAL_2 = 100
    CHECK_NORMAL_3 = 400
    YEARS = range(1, 10000)
    year = int(date.split(".")[-1])
    if year in YEARS and year % CHECK_NORMAL_1 == 0 and year % CHECK_NORMAL_2 != 0 or year % CHECK_NORMAL_3 == 0:
        return True
    return False


def check_year(year: str) -> bool:
    try:
        date = datetime.strptime(year, "%d.%m.%Y").date()
        return True
    except:
        return False


def date_validator(date: str) -> str:
    if check_year(date):
        if _check_leap_year(date):
            return f'{date[-4::]} г. високосный год'
        else:
            return f'{date[-4::]} г. не является високосным'
    else:
        return 'Дата заполнена некорректно'


# data = '25.05.2001'
# print(date_validator(data))

# task001.py 25.05.2001
print(date_validator(argv[1]))
