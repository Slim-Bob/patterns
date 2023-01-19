# Пример поведенческого шаблона проектирования программ «Цепочка обязанностей», который предназначенный
# для организации в системе уровней ответственности.

from __future__ import annotations
from abc import ABCMeta, abstractmethod
from enum import Enum


class Command(Enum):
    DESIGNER = 'designer'
    CARPENTERS = 'carpenters'
    FINISH_WORKER = 'finish worker'
    BEAUTIFUL = 'beautiful'


class IWorker(metaclass=ABCMeta):
    @abstractmethod
    def set_next_worker(self, worker: IWorker) -> IWorker:
        pass

    @abstractmethod
    def execute(self, command: Command) -> str:
        pass


class AbsWorker(IWorker):
    def __init__(self):
        self.__next_worker: IWorker = None

    def set_next_worker(self, worker: IWorker) -> IWorker:
        self.__next_worker = worker
        return worker

    def execute(self, command: Command) -> str:
        if self.__next_worker is not None:
            return self.__next_worker.execute(command)
        return ''


class Designer(AbsWorker):
    def execute(self, command: Command) -> str:
        if command == Command.DESIGNER:
            return f'Проектировщик выполнил команду: {command.value}'
        else:
            return super().execute(command)


class Carpenters(AbsWorker):
    def execute(self, command: Command) -> str:
        if command == Command.CARPENTERS:
            return f'Плотник выполнил команду: {command.value}'
        else:
            return super().execute(command)


class FinishWorker(AbsWorker):
    def execute(self, command: Command) -> str:
        if command == Command.FINISH_WORKER:
            return f'Рабочий выполнил команду: {command.value}'
        else:
            return super().execute(command)


def give_command(worker: IWorker, command: Command):
    result = worker.execute(command)
    if result == '':
        print(f'{command.value} - никто не умеет =(')
    else:
        print(result)


if __name__ == '__main__':
    designer = Designer()
    carpenters = Carpenters()
    finishing_worker = FinishWorker()

    designer.set_next_worker(carpenters).set_next_worker(finishing_worker)

    give_command(designer, Command.DESIGNER)
    give_command(designer, Command.CARPENTERS)
    give_command(designer, Command.FINISH_WORKER)

    give_command(designer, Command.BEAUTIFUL)
