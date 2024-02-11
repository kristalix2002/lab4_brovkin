if __name__ == "__main__":
    class Rocket:
        "Класс-Ракета"

        def __init__(self, name: str, tvp: float):
            self._name = name
            self._tvp = tvp

        def __str__(self):
            return f"Ракета {self._name}. Тяговооруженность ракеты {self._tvp}"

        def __repr__(self):
            return f"{self.__class__.__name__}(name={self._name!r}, tvp={self._tvp!r})"

        @property
        def name(self) -> str:
            return self._name

        """Возвращает название ракеты"""

        @property
        def tvp(self) -> float:
            return self._tvp

        """Возвращает тяговооруженность ракеты"""


    class PTUR(Rocket):
        def __init__(self, name: str, range: float,):
            super().__init__(name=name, range=range)


        def __repr__(self):
            return f"{self.__class__.__name__}(name={self._name!r}, range={self._range!r})"

        @property
        def range(self) -> float:
            return self._range

        """Возвращает макс. высоту сбития"""
        """Метод перегружен, т.к. в случае ЗРК расстоянием будет являться максимальная высота сбития ЛА"""

    pass
