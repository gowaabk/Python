# Напишите программу, которая принимает две строки
# вида “a/b” — дробь с числителем и знаменателем.
# Программа должна возвращать сумму
# и *произведение дробей. Для проверки своего
# кода используйте модуль fractions.

import fractions

def calculate_lcm(x: int, y: int) -> int: #Поиск наименьшего общего кратного
    if x > y:
        greater = x
    else:
        greater = y
    while(True):
        if((greater % x == 0) and (greater % y == 0)):
            lcm = greater
            break
        greater += 1
    return lcm
num1 = input("Введите первую дробь в формате a/b --> ").split("/")
num2 = input("Введите вторую дробь в формате c/d --> ").split("/")

a1 = int(num1[0])
b1 = int(num1[1])
c1 = int(num1[0])
d1 = int(num1[1])

# a1 = 3
# b1 = 15
# c1 = 4
# d1 = 18

smallest_common_multiple = calculate_lcm(b1,d1)
a1_ext = a1*(smallest_common_multiple/b1)
c1_ext = c1*(smallest_common_multiple/d1)

mult = (a1*c1)/(b1*d1)
sum = (a1_ext + c1_ext)/smallest_common_multiple

f1 = fractions.Fraction(a1, b1)
f2 = fractions.Fraction(c1, d1)

print(f"{mult} multiplication *")
print(f"{sum} addition +")
print(f"{f1 * f2} fractions *")
print(f"{f1 + f2} fractions +")