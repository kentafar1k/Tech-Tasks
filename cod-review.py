#исправить ошибки

import math
from abc import ABC, abstractmethod


class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y


class BaseLine(ABC):
    a: Point
    b: Point

    @abstractmethod
    def length(self):
        return math.dist((a.x, a.y), (b.x, b.y))


class Line(BaseLine):
    def __init__(self, a: Point, b: Point):
        super().__init__()
        self.a = a
        self.b = b


p1 = Point(0, 2)
p2 = Point(0, 0)
line = Line(p1, p2)
print(line.length)