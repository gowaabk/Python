# Соберите из созданных на уроке и в рамках домашнего задания функций пакет для работы с файлами разных форматов.

from file import add_name_to_json as np
from file import create_json as cj
from file import make_list_dir
from pathlib import Path


if __name__ == "__main__":
    # path = ".\\Python\\dz8\\file\\"
    # cj.create_json(path)
    # # np.ui()
    # # print(type(np.read_json()))

    # PATH  - путь к каталогу который нужно обойти
    # результат обхода в папке file.
    PATH = "c:\\temp"
    data = make_list_dir.get_data(PATH)
    make_list_dir.save_files(data)
