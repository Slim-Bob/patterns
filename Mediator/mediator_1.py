# Пример поведенческого шаблона проектирования программ «Посредник», который позволяет уменьшить
# связанность множества классов между собой, благодаря перемещению этих связей в один класс-посредник.

from __future__ import annotations
from abc import ABCMeta, abstractmethod


class IMediator(metaclass=ABCMeta):
    @abstractmethod
    def notify(self, emp: Employee, msg: str):
        pass


class Employee(metaclass=ABCMeta):
    def __init__(self, mediator: IMediator):
        self._mediator = mediator

    def set_mediator(self, mediator: IMediator):
        self._mediator = mediator


class Designer(Employee):
    def __init__(self, mediator: IMediator = None):
        super().__init__(mediator)
        self.__is_working = False

    def execute_work(self):
        print('<-Дизайнер в работе')
        self._mediator.notify(self, 'Дизайнер проектирует...')

    def set_work(self, state: bool):
        self.__is_working = state
        if state:
            print('<-Дизайнер освобожден от работы')
        else:
            print('<-Дизайнер занят')


class Director(Employee):
    def __init__(self, mediator: IMediator = None):
        super().__init__(mediator)
        self.__text: str = None

    def give_command(self, txt: str):
        self.__text = txt
        if txt == '':
            print('->Директор знает, что дизайнер уже работает')
        else:
            print(f'->Директор дал команду: {txt}')
        self._mediator.notify(self, txt)


class Controller(IMediator):
    def __init__(self, designer: Designer, director: Director):
        self.__designer = designer
        self.__director = director
        self.__designer.set_mediator(self)
        self.__director.set_mediator(self)

    def notify(self, emp: Employee, msg: str):
        if isinstance(emp, Director):
            if msg == '':
                self.__designer.set_work(False)
            else:
                self.__designer.set_work(True)

        if isinstance(emp, Designer):
            if msg == 'Дизайнер проектирует...':
                self.__director.give_command('')


if __name__ == '__main__':
    designer = Designer()
    director = Director()

    mediator = Controller(designer, director)

    director.give_command('Проектировать')
    print()

    designer.execute_work()