# Пример поведенческого шаблона проектирования программ «Наблюдатель», который позволяет одним объектам
# следить и реагировать на события, происходящие в других объектах.

from abc import ABCMeta, abstractmethod
from typing import List


class IObserver(metaclass=ABCMeta):
    @abstractmethod
    def update(self, price: int):
        pass


class IObservable(metaclass=ABCMeta):
    @abstractmethod
    def add_observer(self, observer: IObserver):
        pass

    @abstractmethod
    def remove_observer(self, observer: IObserver):
        pass

    @abstractmethod
    def notify(self):
        pass


class Product(IObservable):
    def __init__(self, price: int):
        self.__price = price
        self.__observers: List[IObserver] = []

    def change_price(self, price: int):
        self.__price = price
        self.notify()

    def add_observer(self, observer: IObserver):
        self.__observers.append(observer)

    def remove_observer(self, observer: IObserver):
        self.__observers.remove(observer)

    def notify(self):
        for observer in self.__observers:
            observer.update(self.__price)


class Wholesale(IObserver):
    def __init__(self, observable: IObservable):
        self.__product = observable
        self.__product.add_observer(self)

    def update(self, price: int):
        if price < 300:
            print(f'Оптовик закупил товар по цене {price}')
            self.__product.remove_observer(self)


class Buyer(IObserver):
    def __init__(self, observable: IObservable):
        self.__product = observable
        self.__product.add_observer(self)

    def update(self, price: int):
        if price < 350:
            print(f'Покупатель закупил товар по цене {price}')
            self.__product.remove_observer(self)


if __name__ == '__main__':
    product = Product(400)

    wholesale = Wholesale(product)
    buyer = Buyer(product)

    product.change_price(320)
    product.change_price(280)
