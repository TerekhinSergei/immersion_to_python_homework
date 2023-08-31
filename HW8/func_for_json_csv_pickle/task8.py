import os
import json
import csv
import pickle


def convert_txt_to_json(txt_file, json_file):
    with open(txt_file, 'r', encoding='utf-8') as f,\
        open(json_file, "w", encoding='utf-8') as js_f:
        contents = f.readlines()
        my_dict = {}
        for el in contents:
            key, val = el.split("-")
            my_dict[key.title()] = float(val)
        json.dump(my_dict, js_f, separators=(',\n', ':'), ensure_ascii=False)

def fun_dump_json():
    # name = input("введите имя:> ")
    # user_id = input("введите id:> ")
    # level = int(input('введите уровень доступа (1-7):> '))
    name = "Петя"
    user_id = "002"
    level = 4

    with open('task8_2.json', "r", encoding='utf-8') as f:
        res = json.load(f)

    my_dct = {
        "level": level,
        "id": user_id,
        "name": name,
    }

    with open('task8_2.json', "w", encoding='utf-8') as js_f:
        res.append(my_dct)
        json.dump(res, js_f, indent=2, separators=(',', ':'), ensure_ascii=False)


def json_to_csv():
    with open('task8_2.json', "r", encoding='utf-8') as js_f:
        res = json.load(js_f)
        lst = []
        keys = res[0].keys()
        lst.append(keys)
        for el in res:
            vals = el.values()
            lst.append(vals)

    with open('task8_2.csv', "w", newline='', encoding='utf-8') as cs_f:
        writer = csv.writer(cs_f)
        for el in lst:
            writer.writerow(el)


def get_dir_size(path):
    total_size = 0
    for dir_path, dir_names, file_names in os.walk(path):
        for file in file_names:
            fp = os.path.join(dir_path, file)
            total_size += os.path.getsize(fp)
    return total_size


def walker_dir(dir_path):
    res = []
    for root, dirs, files in os.walk(dir_path):
        for name in files:
            full_path = os.path.join(root, name)
            res.append({"parent_directory": root,
                        "object_type": 'File',
                        "name": name,
                        "size_in_bytes": os.path.getsize(full_path)})

        for name in dirs:
            full_path = os.path.join(root, name)
            res.append({"parent_directory": root,
                        "object_type": 'Directory',
                        "name": name,
                        "size_in_bytes": get_dir_size(full_path)})
    return res


if __name__ == '__main__':
    # convert_txt_to_json('task7_3.txt', 'task8_1.json')
    #
    # s = 'n'
    # while s != 'y':
    #     fun_dump_json()
    #     s = input('выход y/n :>')
    #
    # json_to_csv()
    #
    print(get_dir_size('C:\\Users\\Old_Home\\PycharmProjects\\immersion_to_python_home_work'))
    # results = walker_dir('C:\\Users\\Old_Home\\PycharmProjects\\immersion_to_python_home_work\\HW7')
    # print(results)