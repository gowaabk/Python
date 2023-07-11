# Задание №3
# 📌 Напишите класс для хранения информации о человеке:
# ФИО, возраст и т.п. на ваш выбор.
# 📌 У класса должны быть методы birthday для увеличения
# возраста на год, full_name для вывода полного ФИО и т.п. на
# ваш выбор.
# 📌 Убедитесь, что свойство возраст недоступно для прямого
# изменения, но есть возможность получить текущий возраст.

class Human:
    def __init__(self, firstname: str, lastname: str, age: int, gender: str):
        self.firstname = firstname
        self.lastname = lastname
        self.__age = age
        self.gender = gender

    def get_age(self):
        return self.__age
    
    def birthday(self):
        self.__age +=1

    def __str__(self) -> str:
        return f'{self.firstname} {self.lastname} {self.get_age()} {self.gender}'

if __name__ == '__main__':
    h1 = Human("Igor", "Vesel", 35, "M")
    h2 = Human("Vlad", "Zainov", 25, "M")
    h3 = Human("Vera", "Veter", 18, "Ж")

    print(h1)
    print(h2)
    print(h3)

    h1.birthday()
    h3.birthday()

    print(h1)
    print(h2)
    print(h3)