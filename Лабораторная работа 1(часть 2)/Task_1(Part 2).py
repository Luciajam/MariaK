# TODO Написать 3 класса с документацией и аннотацией типов
from typing import Union
import doctest

class Square:
   def __init__(self, lenght: Union[int, float], color: str):
       """

       Инициализация экземпляра класса.

       :param length: Длина стороны квадрата
       :param color: Цвет квадрата

       Примеры:
       >>> square = Square(2, "Red")
       """
       if lenght <=0:
           raise ValueError("Длина не может быть отрицательной")
       self.lenght =lenght
       self.color = color
   def area(self) -> Union[int, float]:
       """
       Метод считает площадь квадрата

       Примеры:
       >>> square = Square(2, "Red")
       >>> square.area()

       """
       ...
   def color_change(self, newcolor:str) -> None:
       """
       Метод меняет цвет фигуры

       :param newcolor: Новый цвет фигуры

       Примеры:
       >>> square = Square(2, "Red")
       >>> square.color_change("Green")
       """
       ...
class Triangle:
    def __init__(self, lenght: Union[int, float], color: str):
        """

        Инициализация экземпляра класса.

        :param length: Длина стороны треугольника
        :param color: Цвет треугольника

        Примеры:
        >>> triangle = Triangle(2, "Red")
        """
        if lenght <= 0:
            raise ValueError("Длина не может быть отрицательной")
        self.lenght = lenght
        self.color = color

    def area(self) -> Union[int, float]:
        """
        Метод считает площадь треугольника

        Примеры:
        >>> triangle = Triangle(2, "Red")
        >>> triangle.area()
        """
        ...

    def color_change(self, newcolor:str) -> None:
        """
        Метод меняет цвет фигуры

        :param newcolor: Новый цвет фигуры

        Примеры:
        >>> triangle = Triangle(2, "Red")
        >>> triangle.color_change("Green")
        """
        ...
class Circle:
    def __init__(self, radius: Union[int, float], color: str):
        """

        Инициализация экземпляра класса.

        :param radius: Радиус круга
        :param color: Цвет круга

        Примеры:
        >>> circle = Circle(2, "Red")
        """
        if radius <= 0:
            raise ValueError("Длина не может быть отрицательной")
        self.radius = radius
        self.color = color

    def area(self) -> Union[int, float]:
        """
        Метод считает площадь круга

        Примеры:
        >>> circle = Circle(2, "Red")
        >>> circle.area()
        """
        ...

    def color_change(self, newcolor:str) -> None:
        """
        Метод меняет цвет фигуры

        :param newcolor: Новый цвет фигуры

        Примеры:
        >>> circle = Circle(2, "Red")
        >>> circle.color_change("Green")
        """
        ...
if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()
    pass
