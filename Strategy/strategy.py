# Пример поведенческого шаблона проектирования программ «Стратегия», который определяет семейство схожих алгоритмов
# и помещает каждый из них в собственный класс. Положительными моментами является то, что паттерн изолирует
# код алгоритмов от остальных классов, алгоритмы можно быстро заменять, во время выполнения программы.

from __future__ import annotations
from abc import ABCMeta, abstractmethod


class IReader(metaclass=ABCMeta):
    @abstractmethod
    def parse(self, url: str):
        pass


class ResourceReader:
    def __init__(self, reader: IReader):
        self._reader = reader

    def set_strategy(self, reader: IReader):
        self._reader = reader

    def read(self, url: str):
        self._reader.parse(url)


class NewsSiteReader(IReader):
    def parse(self, url: str):
        print(f'Парсинг новосного сайта, {url}')


class SocialNetworkReader(IReader):
    def parse(self, url: str):
        print(f'Парсинг социальных сетей, {url}')


class TelegramChannelReader(IReader):
    def parse(self, url: str):
        print(f'Парсинг каналов телеграм, {url}')


if __name__ == '__main__':
    resource_reader = ResourceReader(NewsSiteReader())
    resource_reader.read('123456')

    resource_reader.set_strategy(SocialNetworkReader())
    resource_reader.read('123456')

    resource_reader.set_strategy(TelegramChannelReader())
    resource_reader.read('123456')
