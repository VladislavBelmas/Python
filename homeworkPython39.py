from abc import ABC, abstractmethod
import math


class InvalidSizeError(ValueError):
    """
    Исключение для некорректных размеров фигуры.

    Выбрасывается, если переданы отрицательные значения
    радиуса, ширины или высоты.
    """
    pass



class Shape(ABC):
    """
    Абстрактный базовый класс геометрической фигуры.

    Требует реализации метода area().
    """
    @abstractmethod
    def area(self):
        """
        Вычисляет площадь фигуры.

        :return: площадь фигуры
        """

        pass



class Circle(Shape):

    def __init__(self, rad:float):
        """
        Создаёт объект круга.

        :param rad: радиус круга
        :raises InvalidSizeError:
            если радиус отрицательный
        """
        if rad <= 0:
            raise InvalidSizeError("Must be positive")

        self.rad = rad


    def area(self):
        """
        Вычисляет площадь круга.

        :return: площадь круга
        """
        return (self.rad ** 2) * math.pi


class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        """
        Создаёт объект прямоугольника.

        :param width: ширина прямоугольника
        :param height: высота прямоугольника
        :raises InvalidSizeError:
            если ширина или высота отрицательны
        """
        if width < 0 or height < 0:
            raise InvalidSizeError("Must be positive")

        self.width = width
        self.height = height


    def area(self):
        """
        Вычисляет площадь прямоугольника.

        :return: площадь прямоугольника
        """
        return self.height * self.width


shapes = [Circle(3), Rectangle(4, 5)]

for shape in shapes:

    print(f"Area: {shape.area():.2f}")

