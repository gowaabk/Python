# Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток.
# Программа должна подсказывать “больше” или “меньше” после каждой попытки.
# Для генерации случайного числа используйте код:
# from random import randint
# num = randint(LOWER_LIMIT, UPPER_LIMIT)


from random import randint

LOWER_LIMIT = 0
UPPER_LIMIT = 10
number_of_attempts = 10
num = randint(LOWER_LIMIT, UPPER_LIMIT)
count = 0
result = None
# print(num)
print(f"Угадайте загаданное число за {number_of_attempts} попыток")
while count < number_of_attempts:
    count += 1
    print("Попытка номер ", count)
    number = int(
        input(f"Введите число от {LOWER_LIMIT} до {UPPER_LIMIT} --> "))
    if number > num:
        result = "Меньше"
    elif number < num:
        result = "Больше"
    else:
        print("Угадал")
        break
    if count == number_of_attempts:
        result = "Не угадал(("
    print(result)
