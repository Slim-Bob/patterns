# Пример порождающего шаблона проектирования программ «Прототип», который позволяет копировать объекты, не вдаваясь
# в подробности их реализации. Преимуществом паттерна является то, что он позволяет клонировать объекты, не привязываясь
# к их конкретным классам, уменьшает повторяющийся код при инициализации объектов. Однако составные объекты, имеющие
# ссылки на другие классы, клонировать сложнее.

from __future__ import annotations
from copy import deepcopy


class Sheep:
    WEIGHT: str = 'Вес'
    HEIGHT: str = 'Рост'

    def __init__(self, donor: Sheep = None):
        if donor is not None:
            self._name = donor.get_name()
            self._params = deepcopy(donor.get_params())
        else:
            self._name: str = ''
            self._params: dict = {Sheep.WEIGHT: 20, Sheep.HEIGHT: .34}

    def set_name(self, name: str):
        self._name = name

    def get_name(self) -> str:
        return self._name

    def get_params(self) -> dict:
        return self._params

    def set_weight(self, new_weight: int):
        self._params[Sheep.WEIGHT] = new_weight

    def set_height(self, new_height: int):
        self._params[Sheep.HEIGHT] = new_height

    def clone(self) -> Sheep:
        return Sheep(self)

    def __str__(self):
        return f'Sheep: {self._name}, {self._params}'

    def __repr__(self):
        return (f'{self.__class__.__name__}'
                f'(Sheep: {self._name!r}, {self._params!r})')


if __name__ == '__main__':
    sheep_donor: Sheep = Sheep()
    sheep_donor.set_name('Долли')

    sheep_clone: Sheep = sheep_donor.clone()

    print(sheep_donor)
    print(sheep_clone)
