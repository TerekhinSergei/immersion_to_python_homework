'''
Задание №7
✔ Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п.
✔ Каждая группа включает файлы с несколькими расширениями.
✔ В исходной папке должны остаться только те файлы, которые не подошли для сортировки.
'''
import os

EXTENSIONS = { 'video': ['mp4', 'mov', 'avi', 'mkv', 'wmv', 'mpeg', 'flv', 'vob'],
            'image': ['jpg', 'jpeg', 'png', 'bmp', 'psd', 'ico', 'tiff'],
            'text': ['txt', 'doc', 'docx', 'pdf', 'rtf'],
            'data': ['sql', 'csv', 'dat', 'db', 'mdb'],
            'audio': ['mp3', 'wav', 'wma', 'cda', 'ogg', 'flac'],
    }

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


sort_files('Dir_for_sort_files', EXTENSIONS)
