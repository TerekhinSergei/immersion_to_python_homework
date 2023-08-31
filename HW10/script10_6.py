"""
Задание №6
Доработайте задачу 5.
Вынесите общие свойства и методы классов в класс
Животное.
Остальные классы наследуйте от него.
Убедитесь, что в созданные ранее классы внесены правки.
"""


class Animal:
    def __init__(self, kind, name, age):
        self._kind = kind
        self._name = name
        self._age = age

    def get_kind(self):
        return self._kind

    def get_name(self):
        return self._name

    def get_age(self):
        return self._age

    def up_age(self):
        self._age += 1


class Fishes(Animal):

    def __init__(self, kind, name, age, size):
        super().__init__(kind, name, age)
        self._size = size

    def get_specific(self):
        return self._size

    def get_animal_info(self):
        return f'Вид: {self.get_kind()}, кличка: {self.get_name()}, возраст: {self.get_age()} лет,' \
               f' special: {self.get_specific()}'


class Birds(Animal):

    def __init__(self, kind, name, age, color):
        super().__init__(kind, name, age)
        self._color = color

    def get_specific(self):
        return self._color

    def get_animal_info(self):
        return f'Вид: {self.get_kind()}, кличка: {self.get_name()}, возраст: {self.get_age()} лет,' \
               f' special: {self.get_specific()}'


class Mammals(Animal):

    def __init__(self, kind, name, age, spec):
        super().__init__(kind, name, age)
        self._spec = spec

    def get_specific(self):
        return self._spec

    def get_animal_info(self):
        return f'Вид: {self.get_kind()}, кличка: {self.get_name()}, возраст: {self.get_age()} лет,' \
               f' specific: {self.get_specific()}'


if __name__ == '__main__':
    f1 = Fishes('Карась', 'Федя', 1, 15)

    print(f'Вид: {f1.get_kind()}')
    print(f'кличка: {f1.get_name()}')
    print(f'возраст: {f1.get_age()} лет')
    print(f'размер: {f1.get_specific()} см.')

    b1 = Birds('Синичка', 'пеночка', 1, 'зеленый')
    print(f'Вид: {b1.get_kind()}')
    print(f'кличка: {b1.get_name()}')
    print(f'возраст: {b1.get_age()} лет')
    print(f'Цвет: {b1.get_specific()}')
