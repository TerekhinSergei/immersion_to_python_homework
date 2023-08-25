# Добавлена обработка исключения при создании экземпляра
# и изменении ширины и длины сторон прямоугольника
# Добавлено выдуманное исключение при сложении и вычитании прямоугольников

from task13_Exceptions import RectangleAdd, RectangleSub


class Rectangle:
    """
    Класс "Прямоугольник" для выполнения действий с прямоугольниками,
    позволяет сравнивать прямоугольники по площади,
    получить площадь и периметр прямоугольников
    складывать и вычитать прямоугольники
    """

    __slots__ = ('_width', '_length')

    def __init__(self, side_a, side_b=0):
        if side_b == 0:
            side_b = side_a
        try:
            a, b = side_a, side_b
            if side_a <= 0 or side_b <= 0:
                side_b = side_a = 1
                raise ValueError(f"Длина сторон должна быть больше 0. Вы ввели {a} и {b}\n"
                                 f"Стороны будут принят за 1")
        except ValueError as e:
            print(e)
        finally:
            self._width = side_a
            self._length = side_b

    @property
    def width(self):
        return self._width

    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, new_len):
        try:
            if new_len <= 0:
                raise ValueError(f"Длина должна быть больше 0. Вы ввели {new_len}")
        except ValueError as e:
            print(e)
        else:
            self._length = new_len

    @width.setter
    def width(self, new_width):
        try:
            if new_width <= 0:
                raise ValueError(f"Ширина должна быть больше 0. Вы ввели {new_width}")
        except ValueError as e:
            print(e)
        else:
            self._width = new_width

    def get_perimeter(self):
        return 2 * (self._width + self._length)

    def get_area(self):
        return self._width * self._length

    def __add__(self, other):
        """
        сложение прямоугольников, складываются периметры исходных прямоугольников
        :return: экземпляр класса "Rectangle" полученный после сложения периметров
        """
        res = self.get_perimeter() + other.get_perimeter()
        try:
            if res > 100:
                raise RectangleAdd('строна нового прямоугольника больше 100')
        except RectangleAdd as e:
            print(e)
        finally:
            return Rectangle(res)

    def __sub__(self, other):
        """
        вычитание прямоугольников, вычитаются периметры исходных прямоугольников
        :return: экземпляр класса "Rectangle" полученный после вычитания периметров
        """
        res = abs(self.get_perimeter() - other.get_perimeter())
        try:
            if res < 100:
                raise RectangleSub('строна нового прямоугольника меньше 100')
        except RectangleSub as e:
            print(e)
        finally:
            return Rectangle(res)

    def __str__(self):
        res = f'Прямоугольник со сторонами {self._width} и {self._length}'
        return res


rectangle1 = Rectangle(7, 11)
print(rectangle1)
rectangle2 = Rectangle(15, 35)
print(rectangle2)
rectangle3 = rectangle1 + rectangle2
print(rectangle3)
rectangle4 = rectangle1 - rectangle2
print(rectangle4)
rectangle5 = Rectangle(-7, -11)
print(rectangle5)

rectangle1.width = -5
rectangle1.length = -12
print(rectangle1)
