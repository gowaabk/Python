# Напишите программу, которая получает целое
# число и возвращает его шестнадцатеричное
# строковое представление. Функцию hex
# используйте для проверки своего результата.


def num_systems(num: int, number_sys: int) -> str:
    result = ""
    while num >= 1:
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
    return result[::-1]


# bin_system = 2
# oct_system = 8
hex_system = 16
number = 1023
# number = int(input("Введите десятичное число: --> "))
print(num_systems(number, hex_system), "dec == ", hex(number), " hex")
