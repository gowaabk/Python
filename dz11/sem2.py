# Задание №2
# 📌 Создайте класс Архив, который хранит пару свойств.
# Например, число и строку.
# 📌 При нового экземпляра класса, старые данные из ранее
# созданных экземпляров сохраняются в пару списков-
# архивов
# 📌 list-архивы также являются свойствами экземпляра


# Задание №3
# 📌 Добавьте к задачам 1 и 2 строки документации для классов.

class Archive:
    """Сохраняеv данные каждого экземпляра класса в списки numbers и values"""
    numbers = []
    values = []

    def __new__(cls, number: int, value: str):
        """переопределили метод new для сохранения аргументов"""
        instance = super().__new__(cls)
        cls.numbers.append(number)
        cls.values.append(value)
        return instance

    def __init__(self, number: int, value: str):
        """Определили метод инициализации экземпляров класса"""
        self.number = number
        self.value = value

# Задание №4
# 📌 Доработаем класс Архив из задачи 2.
# 📌 Добавьте методы представления экземпляра для программиста
# и для пользователя.



    def __str__(self):
        return f'Номер: {self.number},  Значение: "{self.value}"'

    def __repr__(self):
        return f'Archive ({self.number}, "{self.value}")'


if __name__ == "__main__":
    a_1 = Archive(1, "one")
    # a_2 = Archive(2, "two")
    # print(f'{a_1.numbers} {a_1.values}')
    # print(f'{a_2.numbers} {a_2.values}')

    # help(a_1)

    # a_3 = Archive(3, "three")
    # print(f'{a_3.numbers} {a_3.values}')
    print(a_1.__repr__())
    print(f"{a_1 = }")
    print(a_1)
