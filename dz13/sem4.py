# Задание №4
# 📌 Вспоминаем задачу из семинара 8 про сериализацию данных,
# где в бесконечном цикле запрашивали имя, личный
# идентификатор и уровень доступа (от 1 до 7) сохраняя
# информацию в JSON файл.
# 📌 Напишите класс пользователя, который хранит эти данные в
# свойствах экземпляра.
# 📌 Отдельно напишите функцию, которая считывает информацию
# из JSON файла и формирует множество пользователей


import json


class User():

    def __init__(self, level, user_id, name) -> None:
        self.level = level
        self.user_id = user_id
        self.name = name

    def __str__(self) -> str:
        return f'{self.level} {self.user_id} {self.name}'
    
def _read_json(file_name: str):
    with open(file_name, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data
    
def parse_data(data: dict):
    user_list = set()
    for level, dict_users in data.items():
        for user_id, name in dict_users.items():
            user_list.add(User(level, user_id, name))
    return user_list

if __name__ == "__main__":
    data =_read_json("dz13\\data.json")
    print(*parse_data(data))