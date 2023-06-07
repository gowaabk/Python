# Напишите функцию, которая принимает на вход строку - абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.


def file_prop(path: str) -> tuple:
    path_split = path.split('\\')
    file_split = path_split[-1].split('.')
    extension = file_split[1]
    file_name = file_split[0]
    full_path = '\\'.join(path_split[0:-1])
    return full_path, file_name, extension


path = r"c:\test\my\file.exe"
print(path)

print(file_prop(path))
