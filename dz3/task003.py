# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
# Достаточно вернуть один допустимый вариант. *Верните все возможные варианты комплектации рюкзака.

import itertools

things = {'зажигалка': 2, 'компас': 10, 'фрукты': 50, 'рубашка': 30,
             'термос': 10, 'аптечка': 2, 'куртка': 60, 'бинокль': 4, 'удочка': 12,
             'салфетки': 4, 'бутерброды': 82, 'палатка': 55, 'спальный мешок': 50}

bag = 8
# bag = int(input("Введите размер рюкзака --> "))


# for i, j in things.items():
#     if j <= bag:
#         print(i, j)
#     elif j >= bag:
#         continue
#     bag -= j

count = 0
summ_bag= 0
my_list = list(things.items())
for i in range(len(things)+1):
    for subset in itertools.combinations(my_list, i):
        for k in range(len(subset)):
            summ_bag +=subset[k][1]
        if summ_bag <= bag:
                count +=1
                print(f"№ {count}\t - вес \t  {summ_bag} \t--\t{subset}")
        summ_bag=0
