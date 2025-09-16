import pytest
import math
from mindboxlib import Shape, Circle, Triangle, calculate_area


def test_circle_area():
    circle = Circle(3)
    assert math.isclose(circle.area(), math.pi * 9, rel_tol=1e-9)

def test_circle_invalid_radius():
    with pytest.raises(ValueError):
        Circle(-1)
    with pytest.raises(ValueError):
        Circle(0)

def test_triangle_area():
    triangle = Triangle(3, 4, 5)
    assert math.isclose(triangle.area(), 6.0, rel_tol=1e-9)

def test_triangle_invalid_sides():
    with pytest.raises(ValueError):
        Triangle(1, 2, 5)
    with pytest.raises(ValueError):
        Triangle(-1, 2, 3)
    with pytest.raises(ValueError):
        Triangle(0, 2, 3)

def test_triangle_is_right_angle():
    t1 = Triangle(3, 4, 5)
    assert t1.is_right_angle() is True

    t2 = Triangle(5, 12, 13)
    assert t2.is_right_angle() is True

    t3 = Triangle(2, 2, 3)
    assert t3.is_right_angle() is False

def test_calculate_area_polymorphic():
    circle = Circle(1)
    triangle = Triangle(3, 4, 5)

    assert math.isclose(calculate_area(circle), math.pi, rel_tol=1e-9)
    assert calculate_area(triangle) == 6.0

def test_easy_to_extend():

    class Square:
        def __init__(self, side):
            self.side = side

        def area(self):
            return self.side ** 2

    class Square(Shape):
        def __init__(self, side):
            if side <= 0:
                raise ValueError("Сторона должна быть положительной")
            self.side = side

        def area(self):
            return self.side ** 2

    square = Square(4)
    assert calculate_area(square) == 16