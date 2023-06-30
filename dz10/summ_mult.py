'''Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
Программа должна возвращать сумму и произведение* дробей.
Для проверки своего кода используйте модуль fractions.'''


class Summ:

    def __init__(self, fraction_1: str, fraction_2: str):
        self.fraction_1 = fraction_1
        self.fraction_2 = fraction_2

    def str_to_digit(self, str_fract: str):
        data_A = int(str_fract.split('/')[0])
        data_B = int(str_fract.split('/')[1])
        return data_A, data_B

    def data_sum(self, data1, data2):
        a_ch = self.str_to_digit(data1)[0]
        a_zn = self.str_to_digit(data1)[1]
        b_ch = self.str_to_digit(data2)[0]
        b_zn = self.str_to_digit(data2)[1]
        ch = a_ch * b_zn + b_ch * a_zn
        zn = b_zn * a_zn
        res = (ch, zn)
        return res

    def __str__(self):
        return f'{self.fraction_1} + {self.fraction_2} =  {self.data_sum(self.fraction_1, self.fraction_2)[0]}/{self.data_sum(self.fraction_1, self.fraction_2)[1]}'


class Mult:

    def __init__(self, fraction_1: str, fraction_2: str):
        self.fraction_1 = fraction_1
        self.fraction_2 = fraction_2

    def str_to_digit(self, str_fract: str):
        data_A = int(str_fract.split('/')[0])
        data_B = int(str_fract.split('/')[1])
        return data_A, data_B

    def data_mult(self, data1, data2):
        a_ch = self.str_to_digit(data1)[0]
        a_zn = self.str_to_digit(data1)[1]
        b_ch = self.str_to_digit(data2)[0]
        b_zn = self.str_to_digit(data2)[1]
        res = (a_ch * b_ch, a_zn * b_zn)
        return res

    def __str__(self):
        return f'{self.fraction_1} * {self.fraction_2} =  {self.data_mult(self.fraction_1, self.fraction_2)[0]}/{self.data_mult(self.fraction_1, self.fraction_2)[1]}'


a = '1/2'
b = '3/4'

sum1 = Summ(a, b)
mult1 = Mult(a, b)
print(sum1)
print(mult1)
