# Задание №1
# 📌 Создайте класс Моя Строка, где:
# 📌 будут доступны все возможности str
# 📌 дополнительно хранятся имя автора строки и время создания
# (time.time)

# Задание №3
# 📌 Добавьте к задачам 1 и 2 строки документации для классов.


import time


class MyString(str):
    """Расширяемый класс моя строка."""
    def __new__(cls, value: str, name: str):
        """Расширяем метод new параметрами value и name"""
        instance = super().__new__(cls, value)
        instance.name = name
        instance.created_at = time.time()
        return instance


if __name__ == "__main__":
    mystr = MyString("САМА строка", "dop parametr")
    print(mystr.name)
    print(mystr.created_at)
    print(mystr)
    print(mystr.lower())
    help(MyString)
    help(mystr)
