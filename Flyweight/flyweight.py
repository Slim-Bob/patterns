# Пример структурного шаблона проектирования программ «Легковес», который позволяет вместить бóльшее количество объектов
# в отведённую оперативную память. Легковес экономит память, выделяя и сохраняя общие параметры объектов.
# Однако при использовании данного паттерна расходуется процессорное время на поиск, а также из-за введения
# дополнительных классов усложняется код программы.

from typing import List, Dict, Optional


class Shared:
    def __init__(self, company: str, position: str):
        self.__company = company
        self.__position = position

    @property
    def company(self):
        return self.__company

    @property
    def position(self):
        return self.__position

    def __str__(self):
        return f'{self.__company}_{self.__position}'

    def __repr__(self):
        return (f'{self.__class__.__name__}'
                f'({self.__company}_{self.__position})')


class Unique:
    def __init__(self, name: str, passport: str):
        self.__name = name
        self.__passport = passport

    @property
    def name(self):
        return self.__name

    @property
    def passport(self):
        return self.__passport

    def __str__(self):
        return f'{self.__name}_{self.__passport}'

    def __repr__(self):
        return (f'{self.__class__.__name__}'
                f'({self.__name}_{self.__passport})')


class Flyweight:
    def __init__(self, shared: Shared):
        self.__shared = shared

    def process(self, unique: Unique):
        print(f'Новые данные: общие - {self.__shared} '
              f'и уникальные {unique}')

    def get_data(self) -> str:
        return str(self.__shared)


class FlyweightFactory:
    def __init__(self, shareds: Optional[dict[Shared]] = None):
        self.__flyweights: Dict[str, Flyweight] = {}
        if shareds is not None:
            for shared in shareds:
                shared_key = str(shared)
                if self.__flyweights.get(shared_key) is None:
                    self.__flyweights[shared_key] = Flyweight(shared)

    def get_flyweight(self, shared: Shared) -> Flyweight:
        shared_key = str(shared)
        if self.__flyweights.get(shared_key) is None:
            print(f'Запись отсутствует. Сохраняем по ключу {shared_key}')
            self.__flyweights[shared_key] = Flyweight(shared)
        else:
            print(f'Извлекам запись {shared_key}')
        return self.__flyweights[shared_key]

    def __str__(self):
        count = len(self.__flyweights)
        flyweights_str: str = ''
        for flyweight in self.__flyweights:
            if flyweights_str == '':
                flyweights_str = str(flyweight)
            else:
                flyweights_str += f';\n{str(flyweight)}'
        return f'Количество записей: {count}\n{flyweights_str}'


def add_specialist(ff: FlyweightFactory, company: str, position: str, name: str, passport: str):
    print()
    flyweight = ff.get_flyweight(Shared(company, position))
    flyweight.process(Unique(name, passport))


if __name__ == '__main__':
    ff = FlyweightFactory()

    add_specialist(ff, "Microsoft", "Управляющий", "Боб", "1234")
    add_specialist(ff, "Microsoft", "Управляющий", "Боб", "1235")
    add_specialist(ff, "Google", "Web", "Дэв", "1235")

    print(ff)
