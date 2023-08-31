"""
Напишите программу, которая решает квадратные уравнения даже если дискриминант отрицательный.
Используйте комплексные числа для извлечения квадратного корня.
"""
import doctest
from math import sqrt


def quadratic_equation(a, b, c):
    """решает квадратные уравнения даже если дискриминант отрицательный.
    >>> quadratic_equation(-18, 60, 100)
    'Корни уравнения: x1 = -1.220; x2 = 4.553'
    >>> quadratic_equation(5, -10, 5)
    'Корень уравнения: x = 1.000'
    >>> quadratic_equation(5, 10, 15)
    'Корни уравнения: x1 = (-1+1.4142j); x2 = (-1-1.4142j)'
    """
    d = b ** 2 - 4 * a * c
    if d > 0:
        x1 = (-b + sqrt(d)) / (2 * a)
        x2 = (-b - sqrt(d)) / (2 * a)
        return (f'Корни уравнения: x1 = {x1:.3f}; x2 = {x2:.3f}')
    elif d == 0:
        x1 = -b / (2 * a)
        return (f'Корень уравнения: x = {x1:.3f}')
    else:
        real = round(-b / (2 * a), 4)
        imaginary = round(sqrt(abs(d)) / (2 * a), 4)
        x1 = complex(real, imaginary)
        x2 = complex(real, -imaginary)
        return (f'Корни уравнения: x1 = {x1}; x2 = {x2}')


if __name__ == '__main__':
    print(quadratic_equation(-18, 60, 100))
    # print(quadratic_equation(5, -10, 5))
    # print(quadratic_equation(5, 10, 15))
    doctest.testmod(verbose=True)
