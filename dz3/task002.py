# В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых.
# Не учитывать знаки препинания и регистр символов.
# За основу возьмите любую статью из википедии или из документации к языку.

import re

path = "dz3/task002.txt"

with open(path, "r", encoding="utf-8") as f:
    text = f.read()

text = re.sub(r"\W", " ", text).split()
dict_text = {}

for i in text:
    dict_text.setdefault(i, text.count(i))

new_list = list(dict_text.items())
new_list.sort(key=lambda i: i[1], reverse=True)

for i in enumerate(new_list[:10], 1):
    print(i)
