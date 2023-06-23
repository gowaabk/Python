# Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все вложенные директории.
# Результаты обхода сохраните в файлы json, csv и pickle.
# - Для дочерних объектов указывайте родительскую директорию.
# - Для каждого объекта укажите файл это или директория.
# - Для файлов сохраните его размер в байтах, а для директорий размер файлов в ней с учётом всех вложенных файлов и директорий.

from pathlib import Path
import csv
import json
import pickle
import os


# PATH = "c:\\temp"


def get_data(path):
    list_dict = []
    for root, dirs, files in os.walk(path):
        data = get_objects(root, dirs, files, list_dict)
    return data


def get_objects(root, dirs, files, list_dict):
    new_dict = {}
    temp_root = root.split('\\')[-1]
    # print(temp_root)
    new_dict["name"] = temp_root
    new_dict['type'] = "dir"
    new_dict["dirs"] = root
    new_dict['size'] = os.path.getsize(str(root))
    list_dict.append(new_dict)
    for name in files:
        new_dict = {}
        new_dict["name"] = name
        new_dict['type'] = "file"
        new_dict["dirs"] = root
        new_dict['size'] = os.path.getsize(str(os.path.join(root, name)))
        list_dict.append(new_dict)
    return list_dict


def save_files(data):
    with open('.\\Python\\dz8\\file\\test.json', 'w',  encoding="utf-8") as outfile_json:
        json.dump(data, outfile_json, indent=2, ensure_ascii=False)

    headers = list(data[0])
    with open(".\\Python\\dz8\\file\\test.csv", "w", encoding='utf-8') as outfile_csv:
        file = csv.DictWriter(
            outfile_csv, delimiter=";", lineterminator="\r", fieldnames=headers)
        file.writeheader()
        for d in data:
            file.writerow(d)

    with open(".\\Python\\dz8\\file\\test.pickle", 'wb') as outfile_pickle:
        pickle.dump(data, outfile_pickle)


# print(data)
