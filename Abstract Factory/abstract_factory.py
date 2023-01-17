# Пример порождающего шаблона проектирования программ «Абстрактная фабрика», который предоставляет интерфейс
# взаимосвязанных или взаимозависимых объектов, не специфицируя их конкретных классов. Шаблон применяется в случаях,
# когда программа должна быть не зависимой от процессов и типов создаваемых новых объектов, а также, когда необходимо
# создавать группы взаимосвязанных объектов

from abc import ABCMeta, abstractmethod


class IEngine(metaclass=ABCMeta):
    @abstractmethod
    def release_engine(self):
        pass


class NoneEngine(IEngine):
    def release_engine(self):
        print("двигатель отсутствует")

    def __str__(self):
        return f'двигатель отсутствует'

    def __repr__(self):
        return f'{self.__class__.__name__}(двигатель отсутствует)'


class JapaneseEngine(IEngine):
    def release_engine(self):
        print("японский двигатель")

    def __str__(self):
        return f'японский двигатель'

    def __repr__(self):
        return f'{self.__class__.__name__}(японский двигатель)'


class RussianEngine(IEngine):
    def release_engine(self):
        print('российский двигатель')

    def __str__(self):
        return f'российский двигатель'

    def __repr__(self):
        return f'{self.__class__.__name__}(российский двигатель)'


class ICar(metaclass=ABCMeta):
    @abstractmethod
    def release_car(self, engine: IEngine):
        pass


class JapaneseCar(ICar):
    def __init__(self):
        self._engine = NoneEngine

    def release_car(self, engine: IEngine):
        self._engine = engine
        print(f'Собрали японский автомобиль, {engine}')

    def __str__(self):
        return f'японский автомобиль'

    def __repr__(self):
        return (f'{self.__class__.__name__}(японский автомобиль)'
                f'({self._engine!r})')


class RussianCar(ICar):
    def __init__(self):
        self._engine = NoneEngine

    def release_car(self, engine: IEngine):
        self._engine = engine
        print(f'Собрали российский автомобиль, {self._engine}')

    def __str__(self):
        return f'российский автомобиль'

    def __repr__(self):
        return (f'{self.__class__.__name__}(российский автомобиль)'
                f'({self._engine!r})')


class IFactory(metaclass=ABCMeta):
    @abstractmethod
    def create_engine(self) -> IEngine:
        pass

    @abstractmethod
    def create_car(self) -> ICar:
        pass


class JapaneseFactory(IFactory):
    def create_engine(self) -> IEngine:
        return JapaneseEngine()

    def create_car(self) -> ICar:
        return JapaneseCar()


class RussianFactory(IFactory):
    def create_engine(self) -> IEngine:
        return RussianEngine()

    def create_car(self) -> ICar:
        return RussianCar()


if __name__ == '__main__':
    j_factory = JapaneseFactory()
    j_engine = j_factory.create_engine()
    j_car = j_factory.create_car()

    j_car.release_car(j_engine)

    r_factory = RussianFactory()
    r_engine = r_factory.create_engine()
    r_car = r_factory.create_car()

    r_car.release_car(r_engine)
