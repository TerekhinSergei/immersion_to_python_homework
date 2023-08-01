"""
Добавьте в пакет, созданный на семинаре шахматный модуль.
Внутри него напишите код, решающий задачу о 8 ферзях.
Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга.
Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга.
Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей.
Если ферзи не бьют друг друга верните истину, а если бьют - ложь.

Напишите функцию в шахматный модуль.
Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше.
Проверяйте различный случайные  варианты и выведите 4 успешных расстановки.

"""
# общий шахматный модуль для 6 домашнего задания

import random


def smite_queens(position):
    n = len(position)
    beat = False
    for i in range(n):
        for j in range(i + 1, n):
            if position[i][0] == position[j][0] or position[i][1] == position[j][1] or \
                    abs(position[i][0] - position[j][0]) == abs(position[i][1] - position[j][1]):
                beat = True
    if beat:
        return False  # бьют
    else:
        return True  # Не бьют


# def successful_position(need_count):
#     position = []
#     count = 1
#     count_iter = 0
#     while count <= need_count:
#         count_iter += 1
#         i = 0
#         while i < 8:
#             x = random.randint(1, 8)
#             y = random.randint(1, 8)
#             if [x, y] not in position:
#                 position.append([x, y])
#                 i += 1
#         if is_queen_beat(position):
#             print('iter = ', count_iter, position)
#             count += 1
#         position.clear()
# Получилась безумно долгие итерации для вычисления, так как randomint генерирует много одинаковых чисел
# Удалось придумать значительно более быстрый вариант.(см.ниже)
def good_position(need_count):
    position = []
    x_position = [1, 2, 3, 4, 5, 6, 7, 8]
    y_position = [1, 2, 3, 4, 5, 6, 7, 8]
    count = 1
    count_iter = 0
    while count <= need_count:
        count_iter += 1
        random.shuffle(x_position)
        random.shuffle(y_position)
        for k in range(8):
            position.append([x_position[k], y_position[k]])

        if smite_queens(position):
            print(f'iteration = {count_iter}: {position}')
            count += 1
        position.clear()


if __name__ == '__main__':
    print(smite_queens([[1, 1], [2, 7], [3, 5], [4, 8], [5, 2], [6, 4], [7, 6], [8, 3]]))  # Не бьют
    print(smite_queens([[1, 2], [2, 4], [3, 6], [4, 8], [5, 1], [6, 3], [7, 5], [8, 7]]))  # бьют
    good_position(4)
