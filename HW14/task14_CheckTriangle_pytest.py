import pytest
from task14_CheckTriangle_doctest import check_triangle


def test_1():
    assert check_triangle(10, 10, 10) == 'Треугольник существует. Треугольник равносторонний', 'ошибка тест 1'


def test_2():
    assert check_triangle(10, 20, 20) == 'Треугольник существует. Треугольник равнобедренный', 'ошибка тест 2'


def test_3():
    assert check_triangle(15, 20, 30) == 'Треугольник существует. Треугольник разносторонний', 'ошибка тест 3'


def test_4():
    assert check_triangle(30, 15, 10) == 'Треугольник не существует', 'ошибка тест 4'


if __name__ == '__main__':
    pytest.main(['-v'])
