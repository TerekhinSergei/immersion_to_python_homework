"""
Напишите следующие функции:
○ Нахождение корней квадратного уравнения
○ Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.
○ Декоратор, запускающий функцию нахождения корней квадратного
уравнения с каждой тройкой чисел из csv файла.
○ Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл.
"""

import csv
import json
from random import randint
from math import sqrt
from functools import wraps


def create_csv(filename):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        for _ in range(randint(100, 1000)):
            line = []
            for _ in range(3):
                x = 0
                while x == 0:  # Исключаем 0(ноль), чтобы уравнение было с тремя членами
                    x = randint(-100, 100)
                line.append(x)
            writer.writerow(line)


def read_csv(func):
    @wraps(func)
    def wrapper(filename):
        results = []
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                a, b, c = map(int, row)
                results.append(func(a, b, c))
        return results
    return wrapper


def write_log(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        with open('log.json', 'a', encoding='utf-8') as js_f:
            dct = {'func': func.__name__, 'args': args, 'kwargs': kwargs, 'result': result}
            json.dump(dct, js_f, indent=2)
        return result
    return wrapper


@read_csv
@write_log
def quadratic_roots(a, b, c):
    d = b ** 2 - 4 * a * c

    if d > 0:
        x1 = (-b + sqrt(d)) / (2 * a)
        x2 = (-b - sqrt(d)) / (2 * a)
        return x1, x2
    elif d == 0:
        x1 = -b / (2 * a)
        return x1
    else:
        real = round(-b / (2 * a), 4)
        imaginary = round(sqrt(abs(d)) / (2 * a), 4)
        x1 = str(complex(real, imaginary))
        x2 = str(complex(real, -imaginary))
        return x1, x2


create_csv('numbers.csv')
quadratic_roots('numbers.csv')
