# Пример структурного шаблона проектирования программ «Адаптер», предназначенный для организации использования функций
# объекта, недоступного для модификации, через специально созданный интерфейс. Другими словами, он позволяет объектам
# с несовместимыми интерфейсами работать вместе.

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


class AdapterForParrotsScales(IScale):
    # Лично у меня попугай ассоциируется с видом Какаду.
    # Запрос в поисковой системе выдал длину от 30 до 60 см
    # Берем среднее (45 см) и принимаем полученное значение за коэффициент
    COEFFICIENT_CM: float = 45

    def __init__(self, parrots_scales: ParrotsScales):
        self._parrots_scales = parrots_scales

    def get_length(self) -> float:
        return self._parrots_scales.get_parrots() * AdapterForParrotsScales.COEFFICIENT_CM


if __name__ == '__main__':
    parrots: float = 2.5  # Два с половиной попугая

    pScales = ParrotsScales(parrots)
    aParrotsScales = AdapterForParrotsScales(pScales)

    cm = aParrotsScales.get_length()
    print(f'{parrots} попугая равняется {cm} см')