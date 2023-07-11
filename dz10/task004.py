# Задание №4
# 📌 Создайте класс Сотрудник.
# 📌 Воспользуйтесь классом человека из прошлого задания.
# 📌 У сотрудника должен быть:
# ○ шестизначный идентификационный номер
# ○ уровень доступа вычисляемый как остаток от деления
# суммы цифр id на семь

from task003 import Human
import random


class Employee(Human):

    def __init__(self, profession: str, firstname: str, lastname: str, age: int, gender: str):
        super().__init__(firstname, lastname, age, gender)
        self.eml_id = self._gen_number()
        self.sec_level = self._secure_level()
        self.profession = profession

    def _gen_number(self):
        MIN_NUM = 100000
        MAX_NUM = 1000000
        return random.randint(MIN_NUM, MAX_NUM)

    def _secure_level(self):
        LEVEL_NUM = 7
        sec_id = self._gen_number()
        level_num = 0
        while sec_id > 0:
            last_num = sec_id % 10
            level_num += last_num
            sec_id /= 10
        return level_num % LEVEL_NUM

    def __str__(self) -> str:
        return f'{self.eml_id} {self.sec_level} {self.profession} {self.firstname} {self.lastname} {self.get_age()} {self.gender}'


if __name__ == '__main__':
    eml_1 = Employee("Slave", "Igor", "Vesel", 35, "M")

    print(eml_1)
