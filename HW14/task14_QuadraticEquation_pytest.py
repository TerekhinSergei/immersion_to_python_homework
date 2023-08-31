import pytest
from task14_QuadraticEquation_doctest import quadratic_equation


def test_1():
    assert quadratic_equation(-18, 60, 100) == 'Корни уравнения: x1 = -1.220; x2 = 4.553', 'ошибка вычисления D > 0'


def test_2():
    assert quadratic_equation(5, -10, 5) == 'Корень уравнения: x = 1.000', 'ошибка вычисления D = 0'


def test_3():
    assert quadratic_equation(5, 10,
                              15) == 'Корни уравнения: x1 = (-1+1.4142j); x2 = (-1-1.4142j)', 'ошибка вычисления D < 0'


if __name__ == '__main__':
    pytest.main(['-v'])
