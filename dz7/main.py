# 2. Соберите из созданных на уроке и в рамках домашнего задания функций пакет для работы с файлами.

from work_files import rename_group

if __name__ == '__main__':
    rename_group.group_rename(5, 'rtf', 'txt', [2, 6], "somefilename")
