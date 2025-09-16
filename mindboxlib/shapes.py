from abc import ABC, abstractmethod
import math

class Shape(ABC):
    
    @abstractmethod
    def area(self) -> float:
        pass


class Circle(Shape):
    
    def __init__(self, radius: float):
        if radius <= 0:
            raise ValueError("Радиус должен быть положительным числом")
        self.radius = radius

    def area(self) -> float:
        return math.pi * self.radius ** 2


class Triangle(Shape):
    
    def __init__(self, a: float, b: float, c: float):
        if any(side <= 0 for side in (a, b, c)):
            raise ValueError("Стороны должны быть положительными числами")
        if not self._is_valid_triangle(a, b, c):
            raise ValueError("Стороны не образуют треугольник")
        
        self.a = a
        self.b = b
        self.c = c

    @staticmethod
    def _is_valid_triangle(a: float, b: float, c: float) -> bool:
        return a + b > c and a + c > b and b + c > a

    def area(self) -> float:
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def is_right_angle(self) -> bool:
        sides = sorted([self.a, self.b, self.c])
        return math.isclose(sides[0] ** 2 + sides[1] ** 2, sides[2] ** 2, rel_tol=1e-9)


def calculate_area(shape: Shape) -> float:
    return shape.area()