# Пример структурного шаблона проектирования программ «Компоновщик», объединяющий объекты в древовидную
# структуру для представления иерархии. «Компоновщик» позволяет клиентам обращаться к отдельным
# объектам и к группам объектов одинаково.

from __future__ import annotations
from abc import ABCMeta, abstractmethod
from typing import Optional


class Item(metaclass=ABCMeta):
    def __init__(self, name: str):
        self._item_name: str = name
        self._owner: Item = None

    def set_owner(self, owner: Optional[Item] = None):
        self._owner = owner

    @abstractmethod
    def add(self, sub_item: Item):
        pass

    @abstractmethod
    def remove(self, sub_item: Item):
        pass

    def __str__(self):
        return f'Owner={self._owner}, Item={self._item_name}'

    def __repr__(self):
        return (f'{self.__class__.__name__}'
                f'(Owner={self._owner!r}, Item={self._item_name})')


class ClickableItem(Item):
    def __init__(self, name: str):
        super().__init__(name)

    def add(self, sub_item: Item):
        raise Exception('Нельзя добавить подэлемент')

    def remove(self, sub_item: Item):
        raise Exception('Нет подэлементов')


class DropDownItem(Item):
    def __init__(self, name: str):
        super().__init__(name)
        self._children = []

    def add(self, sub_item: Item):
        sub_item.set_owner(self)
        self._children.append(sub_item)

    def remove(self, sub_item: Item):
        sub_item.set_owner()
        self._children.remove(sub_item)

    def __str__(self):
        return f'{super().__str__()}; {self._children}'

    def __repr__(self):
        return (f'{self.__class__.__name__}'
                f'(Owner={self._owner!r}, Item={self._item_name})')


if __name__ == '__main__':
    file: Item = DropDownItem('Файл>')

    create: Item = DropDownItem('Создать>')
    create_how: Item = DropDownItem('Создать как')

    open_: Item = DropDownItem('Открыть')
    exit_: Item = ClickableItem('Выход')

    create.add(create_how)
    file.add(create)
    file.add(open_)
    file.add(exit_)

    print(file)

