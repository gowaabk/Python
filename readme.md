# Урок 1. Основы Python

Папка [Домашнее задание к семинару 1](https://github.com/gowaabk/Python/tree/main/dz1)

1. Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей. Дано a, b, c - стороны предполагаемого треугольника. Требуется сравнить длину каждого отрезка-стороны с суммой двух других. Если хотя бы в одном случае отрезок окажется больше суммы двух других, то треугольника с такими сторонами не существует. Отдельно сообщить является ли треугольник разносторонним, равнобедренным или равносторонним.

2. Напишите код, который запрашивает число и сообщает является ли оно простым или составным. Используйте правило для проверки: “Число является простым, если делится нацело только на единицу и на себя”. Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.

3. Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. Программа должна подсказывать “больше” или “меньше” после каждой попытки. Для генерации случайного числа используйте код:
    from random import randint
    num = randint(LOWER_LIMIT, UPPER_LIMIT)

# Урок 2. Простые типы данных

Папка [Домашнее задание к семинару 2](https://github.com/gowaabk/Python/tree/main/dz2)

1. Решить задачи, которые не успели решить на семинаре.
2. Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление. Функцию hex используйте для проверки своего результата.
2. Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем. Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions

# Урок 3. Коллекции

Папка [Домашнее задание к семинару 3](https://github.com/gowaabk/Python/tree/main/dz3)


1. Решить задачи, которые не успели решить на семинаре.
2. Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами. В результирующем списке не должно быть дубликатов.
3. В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых. Не учитывать знаки препинания и регистр символов. За основу возьмите любую статью из   википедии или из документации к языку.
4. Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения. Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.    Достаточно вернуть один допустимый вариант. *Верните все возможные варианты комплектации рюкзака.

# Урок 4. Функции

Папка [Домашнее задание к семинару 4](https://github.com/gowaabk/Python/tree/main/dz4)


1. Напишите функцию для транспонирования матрицы
2. Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь, где ключ - значение переданного аргумента, а значение - имя аргумента. Если ключ не хешируем, используйте его строковое представление.
3. Возьмите задачу о банкомате из семинара 2. Разбейте её на отдельные операции - функции. Дополнительно сохраняйте все операции поступления и снятия средств в список.

# Урок 5. Интераторы и генераторы

Папка [Домашнее задание к семинару 5](https://github.com/gowaabk/Python/tree/main/dz5)


1. Напишите функцию, которая принимает на вход строку - абсолютный путь до файла. Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.
2. Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины: имена str, ставка int, премия str с указанием процентов вида “10.25%”. В результате получаем словарь с именем в качестве ключа и суммой премии в качестве значения. Сумма рассчитывается как ставка умноженная на процент премии
3. Создайте функцию генератор чисел Фибоначчи (см. Википедию)

# Урок 6. Модули
Папка [Домашнее задание к семинару 6](https://github.com/gowaabk/Python/tree/main/dz6)


1. В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку.
2. Добавьте в пакет, созданный на семинаре шахматный модуль. Внутри него напишите код, решающий задачу о 8 ферзях. Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга. Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга. Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей. Если ферзи не бьют друг друга верните истину, а если бьют - ложь.
3. Напишите функцию в шахматный модуль. Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше. Проверяйте различный случайные варианты и выведите 4 успешных расстановки.

# Урок 7. Файлы и файловая система
Папка [Домашнее задание к семинару 7](https://github.com/gowaabk/Python/tree/main/dz7)


1. Напишите функцию группового переименования файлов. Она должна:
    - принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
    - принимать параметр количество цифр в порядковом номере.
    - принимать параметр расширение исходного файла. Переименование должно работать только для этих файлов внутри каталога.
    - принимать параметр расширение конечного файла.
    - принимать диапазон сохраняемого оригинального имени. Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла. К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.
    
2. Соберите из созданных на уроке и в рамках домашнего задания функций пакет для работы с файлами.

# Урок 8. Сериализация

Папка [Домашнее задание к семинару 8](https://github.com/gowaabk/Python/tree/main/dz8)

1. Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все вложенные директории.
Результаты обхода сохраните в файлы json, csv и pickle.
 - Для дочерних объектов указывайте родительскую директорию.
 - Для каждого объекта укажите файл это или директория.
 - Для файлов сохраните его размер в байтах, а для директорий размер файлов в ней с учётом всех вложенных файлов и директорий.

2. Соберите из созданных на уроке и в рамках домашнего задания функций пакет для работы с файлами разных форматов.

# Урок 9. Декораторы

Папка [Домашнее задание к семинару 9](https://github.com/gowaabk/Python/tree/main/dz9)


1. Напишите следующие функции:
        Нахождение корней квадратного уравнения <br>
        Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.<br>
        Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла.<br>
        Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл.<br>
2. Соберите пакет с играми из тех файлов, что уже были созданы в рамках курса

# Урок 10. ООП. Начало

Папка [Домашнее задание к семинару 10](https://github.com/gowaabk/Python/tree/main/dz10)

1. Доработаем задачи 5-6. Создайте класс-фабрику.
    - Класс принимает тип животного (название одного из созданных классов) и параметры для этого типа.
    - Внутри класса создайте экземпляр на основе переданного типа и верните его из класса-фабрики.

2. Возьмите 1-3 любые задачи из прошлых семинаров (например сериализация
данных), которые вы уже решали. Превратите функции в методы класса, а
параметры в свойства. Задачи должны решаться через вызов методов экземпляра.

# Урок 11. ООП. Особенности Python

Папка [Домашнее задание к семинару 11](https://github.com/gowaabk/Python/tree/main/dz11)


1.  Добавьте ко всем задачам с семинара строки документации и методы вывода информации на печать.

2.  Создайте класс Матрица. Добавьте методы для:
    - вывода на печать,
    - сравнения,
    - сложения,
    - *умножения матриц

