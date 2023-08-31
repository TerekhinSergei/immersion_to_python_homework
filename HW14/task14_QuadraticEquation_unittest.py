import unittest
from task14_QuadraticEquation_doctest import quadratic_equation


class TestCaseName(unittest.TestCase):

    def test_method_1(self):
        self.assertEqual(quadratic_equation(-18, 60, 100), 'Корни уравнения: x1 = -1.220; x2 = 4.553')

    def test_method_2(self):
        self.assertEqual(quadratic_equation(5, -10, 5), 'Корень уравнения: x = 1.000')

    def test_method_3(self):
        self.assertEqual(quadratic_equation(5, 10, 15), 'Корни уравнения: x1 = (-1+1.4142j); x2 = (-1-1.4142j)')


if __name__ == '__main__':
    unittest.main(verbosity=2)
