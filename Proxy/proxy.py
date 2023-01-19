# Пример структурного шаблона проектирования программ «Заместитель», представляющий объект, который контролирует
# доступ к другому объекту, перехватывая все вызовы к нему. Положительным моментом использования паттерна
# в клиент-серверном приложении является то, что в нем применяется кэширование ранее полученных данных и тем самым
# снижается количество запросов к серверу.

from abc import ABCMeta, abstractmethod
from typing import Dict


class ISite(metaclass=ABCMeta):
    @abstractmethod
    def get_page(self, num: int) -> str:
        pass


class Site(ISite):
    def get_page(self, num: int) -> str:
        return f'Страница №{num}'


class SiteProxy(ISite):
    def __init__(self, site: ISite):
        self.__site = site
        self.__cache: Dict[int, str] = {}

    def get_page(self, num: int) -> str:
        page: str = ''
        if self.__cache.get(num) is not None:
            page = f'Кэш: {self.__cache[num]}'
        else:
            page = self.__site.get_page(num)
            self.__cache[num] = page
        return page


if __name__ == '__main__':
    my_site: ISite = SiteProxy(Site())

    print(my_site.get_page(1))
    print(my_site.get_page(2))
    print(my_site.get_page(3))

    print(my_site.get_page(2))
