"""
My Exception
"""


class TriangleEquilateral(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return self.value


class TriangleIsosceles(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return self.value


class TriangleOrdinary(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return self.value


class TriangleExists(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return self.value


class RectangleAdd(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return self.value


class RectangleSub(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return self.value