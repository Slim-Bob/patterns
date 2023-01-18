from __future__ import annotations
from abc import ABCMeta, abstractmethod


class IScale(metaclass=ABCMeta):
    @abstractmethod
    def get_length(self) -> float:
        pass


class RussianScales(IScale):
    def __init__(self, cw: float):
        self._current_weight = cw

    def get_length(self) -> float:
        return self._current_weight


class ParrotsScales:
    def __init__(self, parrots: float):
        self._parrots = parrots

    def get_parrots(self) -> float:
        return self._parrots


class AdapterForParrotsScales(ParrotsScales, IScale):
    # Лично у меня попугай ассоциируется с видом Какаду.
    # Запрос в поисковой системе выдал длину от 30 до 60 см
    # Берем среднее (45 см) и принимаем полученное значение за коэффициент
    COEFFICIENT_CM: float = 45

    def __init__(self, parrots: float):
        super().__init__(parrots)

    def get_length(self) -> float:
        return super().get_parrots() * AdapterForParrotsScales.COEFFICIENT_CM


if __name__ == '__main__':
    parrots: float = 2.5  # Два с половиной попугая

    aParrotsScales = AdapterForParrotsScales(parrots)

    cm = aParrotsScales.get_length()
    print(f'{parrots} попугая равняется {cm} см')