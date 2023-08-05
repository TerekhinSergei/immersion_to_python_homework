import os
from string import ascii_lowercase
from random import randbytes
from random import randint, choices, uniform


def write_pair_nums(filename, lines):
    with open(filename, 'w', encoding='utf-8') as f:
        print(type(f))
        for _ in range(lines):
            int_num = randint(-1000, 1000)
            float_num = uniform(-1000, 1000)
            f.write(f'{int_num} | {float_num:.2f}\n')


def write_random_name(count_names: int):
    alfabet = ''.join([chr(char) for char in range(ord('а'), ord('я') + 1)])
    vowels = 'аеиоуыэюя'
    count = 0
    str_names = ""
    while count != count_names:
        word = choices(alfabet, k=randint(4, 7))
        if any(item in vowels for item in word):
            str_names += ''.join(word).capitalize() + '\n'
            count += 1
    with open('task7_2.txt', 'a', encoding='utf-8') as f:
        f.write(str_names)


def my_func():
    with open('task7_1.txt', 'r', encoding='utf-8') as f_nums, \
            open('task7_2.txt', 'r', encoding='utf-8') as f_names:
        nums = f_nums.readlines()
        names = f_names.readlines()

    for_write = []
    long = max(len(nums), len(names))
    i = 0
    while len(nums) != len(names):
        if len(nums) > len(names):
            names.extend(names[:len(nums) - len(names)])
        else:
            nums.extend(nums[:len(names) - len(nums)])

    while i < long:
        name = names[i]
        num = nums[i]
        a, b = map(float, num.split('|'))
        mult = a * b

        if mult >= 0:
            for_write.append(f'{name.upper().rstrip()} - {round(mult)}\n')
        else:
            for_write.append(f'{name.lower().rstrip()} - {abs(mult)}\n')
        i += 1

    with open("task7_3.txt", 'w', encoding='utf-8') as f:
        f.writelines(for_write)


def func(ext, min_len=6, max_len=30, min_rand_bytes=256, max_rand_bytes=4096, files=42):
    for i in range(files):
        name = ''.join(choices(ascii_lowercase, k=randint(min_len, max_len))) + ext
        size = randint(min_rand_bytes, max_rand_bytes)
        with open(name, 'wb') as f:
            f.write(randbytes(size))


def func_2(files=10, **kwargs):
    dct = kwargs
    val = []
    for k, v in dct.items():
        val.append(v)
    for i in range(files):
        ext = str(*choices(val))
        func(ext, files=1, min_len=6, max_len=10, min_rand_bytes=256, max_rand_bytes=2048)


def func_3(new_dir):
    my_path = os.getcwd() + new_dir
    try:
        os.makedirs(my_path)
        os.chdir(my_path)
    except FileExistsError:
        os.chdir(my_path)
    func_2(15, a='.txt', b='.pdf', c='.png')
    os.chdir('..')

def sort_files(directory, extensions):

    file_list = [file.split('.') for dirs, folders, files in os.walk(directory) for file in files]

    for (name, ext) in file_list:
        for k, v in extensions.items():
            if ext in v:
                new_dir = os.path.join(os.getcwd(), directory, k)
                old_place = os.path.join(directory, f'{name}.{ext}')
                new_place = os.path.join(new_dir, f'{name}.{ext}')
                if os.path.isdir(new_dir):
                    os.replace(old_place, new_place)
                else:
                    os.makedirs(new_dir)
                    os.replace(old_place, new_place)  

def rename_files(final_name: str, len_number: int, start_ext: str, final_ext: str,
                 old_name: list[int, int], work_dir=os.getcwd()):
    start_letter, end_letter = old_name
    for dirs, folders, files in os.walk(work_dir):
        for i, file in enumerate(files):
            if file.endswith(start_ext):
                old_name = os.path.join(dirs, file)
                new_name = (f'{dirs}\\{file[start_letter:end_letter]}{final_name}'
                            f'{str(i).zfill(len_number)}.{final_ext}')
                os.rename(old_name, new_name)



if __name__ == '__main__':
    EXTENSIONS = { 'video': ['mp4', 'mov', 'avi', 'mkv', 'wmv', 'mpeg', 'flv', 'vob'],
            'image': ['jpg', 'jpeg', 'png', 'bmp', 'psd', 'ico', 'tiff'],
            'text': ['txt', 'doc', 'docx', 'pdf', 'rtf'],
            'data': ['sql', 'csv', 'dat', 'db', 'mdb'],
            'audio': ['mp3', 'wav', 'wma', 'cda', 'ogg', 'flac'],}

    write_pair_nums('task7_1.txt', 20)
    # write_random_name(6)
    # my_func()
    # func(ext, files=1, min_len=6, max_len=10, min_rand_bytes=256, max_rand_bytes=2048)
    # func_2(15, a='.txt', b='.pdf', c='.png')
    # func_3('\\task6')
    # sort_files('Dir_for_sort_files', EXTENSIONS)
    # rename_files('_file', 2, 'pdf', 'my_pdf', [1, 5], 'Files_folder_7')
