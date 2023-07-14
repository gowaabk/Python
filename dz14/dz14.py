
    # Возьмите 1-3 задачи из тех, что были на прошлых семинарах или в домашних заданиях.
    # Напишите к ним тесты. 2-5 тестов на задачу в трёх вариантах:
    #     doctest,
    #     unittest,
    #     pytest.


import doctest
import unittest
import pytest


def num_systems(num: int, number_sys: int) -> str:

    '''
    # doctest
    >>> num_systems(15 ,16)
    'F'
    >>> num_systems(7, 10)
    '7'
    >>> num_systems(255, 16)
    'FF'
    '''
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

# Unitest
class TestNumber(unittest.TestCase):
    def test_hex(self):
        self.assertEqual(num_systems(65535, 16), "FFFF" ,msg="HEX test")

    def test_dec(self):
        self.assertEqual(num_systems(10, 10), "10" ,msg="DEC test")

    def test_bin(self):
        self.assertEqual(num_systems(7, 2),"111", msg="BIN test")
    
if __name__ == "__main__":
    doctest.testmod(verbose =True)
    unittest.main(verbosity = 2)


# # bin_system = 2
# # oct_system = 8
# hex_system = 16
# number = 1023
# # number = int(input("Введите десятичное число: --> "))
# print(num_systems(number, hex_system), "dec == ", hex(number), " hex")