from __future__ import  annotations
from abc import ABCMeta, abstractmethod
from typing import Deque


class IMemento(metaclass=ABCMeta):
    @abstractmethod
    def get_dollar(self) -> float:
        pass

    @abstractmethod
    def get_euro(self) -> float:
        pass


class ExchangeMemento(IMemento):
    def __init__(self, dollar: float = 0, euro: float = 0):
        self.__dollar = dollar
        self.__euro = euro

    def get_dollar(self) -> float:
        return self.__dollar

    def get_euro(self) -> float:
        return self.__euro


class Exchange:
    def __init__(self, dollar: float = 0, euro: float = 0):
        self.__dollar = dollar
        self.__euro = euro

    def get_dollar(self) -> float:
        return self.__dollar

    def get_euro(self) -> float:
        return self.__euro

    def sell(self):
        if self.__dollar > 0:
            self.__dollar -= 1

    def buy(self):
        self.__euro += 1

    def save(self) -> ExchangeMemento:
        return ExchangeMemento(self.__dollar, self.__euro)

    def restore(self, exchange_memento: IMemento):
        self.__dollar = exchange_memento.get_dollar()
        self.__euro = exchange_memento.get_euro()

    def __str__(self):
        return f'Доллары: {self.__dollar}, Евры: {self.__euro}'

    def __repr__(self):
        return (f'{self.__class__.__name__}'
                f'(Доллары: {self.__dollar}, Евры: {self.__euro})')


class Memory:
    def __init__(self, exchange: Exchange):
        self.__exchange = exchange
        self.__history: Deque[IMemento] = []

    def backup(self):
        self.__history.append(self.__exchange.save())

    def undo(self):
        if len(self.__history) == 0:
            return
        else:
            self.__exchange.restore(self.__history.pop())


if __name__ == '__main__':
    exchange = Exchange(dollar=15.5, euro=16.5)

    memory = Memory(exchange)
    print(exchange)

    exchange.sell()
    exchange.buy()
    print(exchange)
    memory.backup()

    exchange.sell()
    exchange.buy()
    print(exchange)
    memory.backup()

    memory.undo()
    print(exchange)

    memory.undo()
    print(exchange)

