"""
Создайте класс Матрица. Добавьте методы для:
- вывода на печать,
- сравнения,
- сложения,
- умножения матриц
"""


class Matrix:

    def __init__(self, matrix):
        self.matr = matrix

    def __eq__(self, other):
        if len(self.matr) != len(other.matr) or len(self.matr[0]) != len(other.matr[0]):
            return f'Error: Данные матрицы разных размеров. Сравнение невозможно'
        else:
            for i in range(len(self.matr)):
                for j in range(len(self.matr[0])):
                    if self.matr[i][j] != other.matr[i][j]:
                        return False
            return True

    def __add__(self, other):
        if len(self.matr) != len(other.matr) or len(self.matr[0]) != len(other.matr[0]):
            return f'Error: сложение невозможно - матрицы разных размеров'
        else:
            s_matr = [[self.matr[i][j] + other.matr[i][j] for j in range(len(self.matr[0]))] for i in
                      range(len(self.matr))]
            return Matrix(s_matr)

    def __mul__(self, other):
        if len(self.matr[0]) != len(other.matr):
            return f'Error: Данные матрицы нельзя перемножить'
        else:
            m_matr = [[sum(i * j for i, j in zip(i_row, j_col)) for j_col in zip(*other.matr)] for i_row in self.matr]
            return Matrix(m_matr)

    def __str__(self):
        m = ''
        for i in range(len(self.matr)):
            m += str(self.matr[i]) + '\n'
        return m


m_1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [0, 1, 2]]

m_2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]

m_3 = [[2, 4, 6, 8], [1, 3, 5, 7], [0, 9, 10, 11]]

matrix_1 = Matrix(m_1)
matrix_2 = Matrix(m_2)
matrix_3 = Matrix(m_3)

print('вывода на печать:')
print(f'matrix_1:\n{matrix_1}')
print(f'matrix_3:\n{matrix_3}')

print('Cравнение матриц:')
print(f'matrix_1 == matrix_2: {matrix_1 == matrix_2}')
print(f'matrix_2 == matrix_3: {matrix_2 == matrix_3}')
print(f'matrix_1 == matrix_1: {matrix_1 == matrix_1}')
print()
print('Cложение матриц:')
print(f'matrix_1 + matrix_2:\n{matrix_1 + matrix_2}')
print(f'matrix_3 + matrix_2:\n{matrix_3 + matrix_2}')
print()
print('Умножение матриц:')
print(f'matrix_1 * matrix_3:\n{matrix_1 * matrix_3}')
print(f'matrix_1 * matrix_2:\n{matrix_1 * matrix_2}')
