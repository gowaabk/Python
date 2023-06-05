# Напишите функцию принимающую на вход только ключевые
# параметры и возвращающую словарь, где ключ — значение
# переданного аргумента, а значение — имя аргумента. Если
# ключ не хешируем, используйте его строковое представление.

def make_dicts(**kwargs):
    animals = dict()
    for i, j in kwargs.items():
        if isinstance(j, (list, dict, set, bytearray)):
            j = str(j)
        animals[j] = i
    return animals


print(make_dicts(bull='Red Neck', horses={"Star": 2, "Bow": 3}, dogs=["Jess", "Ness", "Pol"],
                 cats={"Lily", "Glass"}))
