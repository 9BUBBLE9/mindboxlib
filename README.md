# MindBoxLib — библиотека для вычисления площади геометрических фигур

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Tests](https://img.shields.io/badge/Tests-7%2F7%20passed-brightgreen)

> Лёгкая, расширяемая Python-библиотека с поддержкой полиморфизма, юнит-тестами и возможностью добавления новых фигур без изменения ядра.

---

## Возможности

- Вычисление площади **круга** по радиусу
- Вычисление площади **треугольника** по трём сторонам
- Проверка, является ли треугольник **прямоугольным**
- **Полиморфное** вычисление площади — без знания типа фигуры на этапе компиляции
- **Легко расширяема** — добавление новых фигур без изменения существующего кода
- **Полное покрытие юнит-тестами** (7/7 тестов)

---

## Установка

### 1. Клонируйте репозиторий:

```bash
git clone https://github.com/9BUBBLE9/mindboxlib.git
cd mindboxlib
```
### 2. Установите библиотеку в режиме разработки(Рекомендуется использовать виртуальное окружение):
```
pip install -e .
```
## Использование
# Пример 1: Площадь круга и треугольника
from mindboxlib import Circle, Triangle, calculate_area
# Создаём фигуры
circle = Circle(radius=5)
triangle = Triangle(a=3, b=4, c=5)
# Полиморфное вычисление площади — без знания типа!
print("Площадь круга:", calculate_area(circle))     # ~78.54
print("Площадь треугольника:", calculate_area(triangle))  # 6.0
# Проверка прямоугольного треугольника
print("Треугольник прямоугольный?", triangle.is_right_angle())  # True

# Пример 2: Добавление новой фигуры (расширяемость)
from mindboxlib import Shape, calculate_area

class Square(Shape):
    def __init__(self, side: float):
        if side <= 0:
            raise ValueError("Сторона должна быть положительной")
        self.side = side
    def area(self) -> float:
        return self.side ** 2
# Новая фигура сразу совместима!
square = Square(4)
print("Площадь квадрата:", calculate_area(square))  # 16.0

### 3. Запуск тестов
```bash
pip install pytest
pytest
```
# Ожидаемый вывод:
collected 7 items

tests/test_shapes.py ....... [100%]

========================== 7 passed in 0.05s ==========================

### 4. Архитектура
Shape — абстрактный базовый класс
Circle, Triangle — конкретные реализации
calculate_area(shape: Shape) — полиморфная функция
Все фигуры легко расширяемы через наследование

### 5. Требования
Python 3.8+
setuptools, wheel (устанавливаются автоматически при pip install -e .)
pytest — только для запуска тестов
