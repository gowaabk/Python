# Напишите функцию группового переименования файлов.
# Она должна:
# - принимать параметр желаемое конечное имя файлов.
# При переименовании в конце имени добавляется порядковый номер.
# - принимать параметр количество цифр в порядковом номере.
# - принимать параметр расширение исходного файла.
# Переименование должно работать только для этих файлов внутри каталога.
# - принимать параметр расширение конечного файла.
# - принимать диапазон сохраняемого оригинального имени.
# Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла.
# К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.

import os
from pathlib import Path


def group_rename(len_name: int, extension_old: str, new_extension_new: str, interval: list[int], new_name='') -> None:
    count = 0
    # Установка пути для моего каталога test
    path = '.\\Python\\dz7\\test\\'
    saved_cwd = os.getcwd()  # сохраняем текущий путь
    # Временно меняем путь на каталог тест
    os.chdir(path)
    for file in os.listdir():
        # print(file)
        # print(file.endswith(extension_old))
        # print(Path(file))
        if file.endswith(extension_old):
            count += 1
            Path(file).rename(f"{file.split('.')[0][interval[0]:interval[1]]}{new_name}{count:0>{len_name}}."
                              f"{new_extension_new}")
    os.chdir(saved_cwd)  # Возвращаем изначальный путь


