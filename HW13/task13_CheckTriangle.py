# Проверка существуования треуголника, реализация через исключения.

from task13_Exceptions import TriangleEquilateral, TriangleIsosceles, TriangleOrdinary, TriangleExists


class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def check_triangle(self):
        try:
            if self.a == self.b == self.c:
                raise TriangleEquilateral('Треугольник существует. Треугольник равносторонний')
            elif self.a == self.b or self.a == self.c or self.c == self.b:
                raise TriangleIsosceles('Треугольник существует. Треугольник равнобедренный')
            elif self.a + self.c > self.b and self.a + self.b > self.c and self.b + self.c > self.a:
                raise TriangleOrdinary('Треугольник существует. Треугольник разносторонний')
            else:
                raise TriangleExists('Треугольник не существует')
        except TriangleEquilateral as e:
            print(e)
        except TriangleIsosceles as e:
            print(e)
        except TriangleOrdinary as e:
            print(e)
        except TriangleExists as e:
            print(e)

# print('Опредление существования треугольника со сторонами a,b,c')
# a = float(input('введите длину стороны a: '))
# b = float(input('введите длину стороны b: '))
# c = float(input('введите длину стороны c: '))
t_1 = Triangle(10, 10, 10)
t_2 = Triangle(20, 10, 20)
t_3 = Triangle(15, 20, 30)
t_4 = Triangle(30, 15, 10)
print(t_1.check_triangle())
print(t_2.check_triangle())
print(t_3.check_triangle())
print(t_4.check_triangle())
