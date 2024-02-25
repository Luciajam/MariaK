if __name__ == "__main__":
    class Toy:
        """
        Класс описывает модель игрушки.

        """
        def __init__(self, name: str, shape: str, height: float, weight: float, color: str):
            """
            Инициализация экземпляра класса.

            :param name: Имя игрушки
            :param shape: Форма игрушки
            :param height: Высота игрушки
            :param weight: Вес игрушки
            :param color: Цвет игрушки

            """
            self.name = name
            self.shape = shape
            self.height = height
            self.weight = weight
            self.color = color
            self.is_taken: bool = False

        def take(self):
            """
            Метод поднимает игрушку.

            """

            if not self.is_taken:

                self.is_taken = True
                print("Вы подняли игрушку")

            else:

                print("Игрушка уже поднята")

        def put(self):
            """
            Метод опускает игрушку.

            """
            if self.is_taken:

                self.is_taken = False
                print("Вы опустили игрушку")

            else:

                print("Игрушка уже лежит")

        def __str__(self) -> str:
            """
            Магический метод. Определяет поведение функции str(), вызванной для экземпляра класса.

            """
            return f'Игрушка по имени {self.name}'

        def __repr__(self) -> str:
            """
            Магический метод. Возвращает строку, показывающую, как может быть инициализирован класс.

            """
            return f'toy(name={self.name!r}, shape={self.shape!r}, height={self.height!r}, weight={self.weight!r}, color={self.color!r})'


    class Plushy_toy(Toy):
        """
        Класс описывает модель плюшевой игрушки.

        """
        def __init__(self, name: str, shape: str, height: float, weight: float, color: str, material: str):
            """
            Инициализация экземпляра класса. Перегружен из-за добавления нового атрибута.

            :param name: Имя плюшевой игрушки
            :param shape: Форма плюшевой игрушки
            :param height: Высота плюшевой игрушки
            :param weight: Вес плюшевой игрушки
            :param color: Цвет плюшевой игрушки
            :param material: Материал игрушки

            """
            super().__init__(name, shape, height, weight, color)
            self.material = material

        def hug(self):
            """
            Метод обнимает игрушку.

            """
            print(f'{self.name} издаёт довольные звуки:3')

        def take(self):
            """
            Метод поднимает игрушку. Перегружен для учёта особенности реакции на поднятие плюшевой игрушки.

            """
            if not self.is_taken:

                self.is_taken = True
                print("Вы подняли игрушку. Теперь она свисает в ваших руках")

            else:

                print("Игрушка уже поднята и свисает в ваших руках")

        def __str__(self) -> str:
            """
            Магический метод. Определяет поведение функции str(), вызванной для экземпляра класса. Перегружен для отображения типа игрушки.

            """
            return f'Мягкая игрушка по имени {self.name}'

        def __repr__(self) -> str:
            """
            Магический метод. Возвращает строку, показывающую, как может быть инициализирован класс. Перегружен из-за добавления нового атрибута.

            """
            return f'toy(name={self.name!r}, shape={self.shape!r}, height={self.height!r}, weight={self.weight!r}, color={self.color!r}, material={self.material!r})'


    class Plastic_toy(Toy):
        """
        Класс описывает модель пластиковой игрушки.

        """
        def __init__(self, name: str, shape: str, height: float, weight: float, color: str, plastic_type: str):
            """
            Инициализация экземпляра класса. Метод перегружен из-за добавления нового атрибута.

            :param name: Имя пластиковой игрушки
            :param shape: Форма пластиковой игрушки
            :param height: Высота пластиковой игрушки
            :param weight: Вес пластиковой игрушки
            :param color: Цвет пластиковой игрушки
            :param plastic_type: Тип пластика пластиковой игрушки

            """
            super().__init__(name, shape, height, weight, color)
            self.plastic_type = plastic_type
            self.is_damaged = False

        def scratch(self):
            """
            Метод царапает игрушку.

            """
            if not self.is_damaged:

                self.is_damaged = True
                print(f"На пластиковой игрушке {self.name} появились царапины")

            else:

                print(f"Вы оставили ещё пару царапин на пластиковой игрушке {self.name}")

        def put(self):
            """
            Метод кладёт игрушку. Перегружен для учёта особенности реакции пластиковой игрушки при опускании.

            """
            if self.is_taken:

                self.is_taken = False
                print("Вы со стуком опустили пластиковую игрушку")

            else:

                print("Игрушка уже лежит")

        def __repr__(self) -> str:
            """
            Магический метод. Возвращает строку, показывающую, как может быть инициализирован класс. Перегружен  из-за добавления нового атрибута.

            """
            return f'toy(name={self.name!r}, shape={self.shape!r}, height={self.height!r}, weight={self.weight!r}, color={self.color!r}, plastic_type={self.plastic_type!r})'

    plushy_toy1 = Plushy_toy('Zoe', 'Dog', 30, 0.15, 'Black', 'Wool')

    plastic_toy1 = Plastic_toy('Lego', 'Rectangle', 5, 0.05, 'Yellow', 'ABS')

    plushy_toy1.put()
    plushy_toy1.take()
    plushy_toy1.put()
    plushy_toy1.hug()

    plastic_toy1.put()
    plastic_toy1.take()
    plastic_toy1.put()
    plastic_toy1.scratch()
    plastic_toy1.scratch()
    pass
