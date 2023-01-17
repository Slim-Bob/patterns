# Пример порождающего шаблона проектирования программ «Строитель», который предоставляет способ создания
# составного объекта. Он отделяет конструирование сложного объекта от его представления так, что в результате
# одного и того же процесса конструирования могут получаться разные представления.

from abc import ABCMeta, abstractmethod
from copy import deepcopy


class Phone:
    def __init__(self):
        self._data: str = ''

    def about_phone(self) -> str:
        return self._data

    def add_data(self, new_data: str):
        self._data += new_data

    def __str__(self):
        return f'Телефон: {self._data}'

    def __repr__(self):
        return f'{self.__class__.__name__}(Телефон: {self._data})'


class IDeveloper(metaclass=ABCMeta):
    def __init__(self):
        self._phone: Phone = Phone()

    @abstractmethod
    def create_display(self):
        pass

    @abstractmethod
    def create_box(self):
        pass

    @abstractmethod
    def system_install(self):
        pass

    def get_phone(self) -> Phone:
        return deepcopy(self._phone)


class SamsungDeveloper(IDeveloper):
    def create_display(self):
        self._phone.add_data("Произведен дисплей Samsung; ")

    def create_box(self):
        self._phone.add_data("Произведен корпус Samsung; ")

    def system_install(self):
        self._phone.add_data("Установлен Tizen; ")


class AppleDeveloper(IDeveloper):
    def create_display(self):
        self._phone.add_data("Произведен дисплей Sam...Apple; ")

    def create_box(self):
        self._phone.add_data("Произведен корпус Apple; ")

    def system_install(self):
        self._phone.add_data("Установлен iOS; ")


class Director:
    def __init__(self, developer: IDeveloper):
        self._developer = developer

    def set_developer(self, developer: IDeveloper):
        self._developer = developer

    def mount_only_phone(self) -> Phone:
        self._developer.create_box()
        self._developer.create_display()
        return self._developer.get_phone()

    def mount_full_phone(self) -> Phone:
        self._developer.create_box()
        self._developer.create_display()
        self._developer.system_install()
        return self._developer.get_phone()


if __name__ == '__main__':
    samsung_dev = SamsungDeveloper()

    director = Director(samsung_dev)

    phone = director.mount_only_phone()
    print(phone)

    phone = director.mount_full_phone()
    print(phone)

    apple_dev = AppleDeveloper()
    director.set_developer(apple_dev)

    phone = director.mount_only_phone()
    print(phone)

    phone = director.mount_full_phone()
    print(phone)

