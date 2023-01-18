# Пример структурного шаблона проектирования программ «Декоратор», предназначенный для динамического
# подключения объекту дополнительного поведения. Шаблон «Декоратор» предоставляет гибкую альтернативу
# практике создания подклассов с целью расширения функциональности.

from __future__ import annotations
from abc import ABCMeta, abstractmethod
from typing import Optional
from string import Template


class IProcessor(metaclass=ABCMeta):
    @abstractmethod
    def process(self):
        pass


class Transmitter(IProcessor):
    def __init__(self, data: str):
        self._data = data

    def process(self):
        _ = Template('Данные $data переданы по каналу связи')
        # _.substitute(data=self._data)
        print(_.substitute(data=self._data))


class Shell(IProcessor):
    def __init__(self, processor: IProcessor):
        self._processor = processor

    @abstractmethod
    def process(self):
        self._processor.process()


class SlimBobCoder(Shell):
    def __init__(self, processor: IProcessor):
        super().__init__(processor)

    def process(self):
        print('Slim-Bob добавил код до...')
        self._processor.process()
        print('Slim-Bob добавил код после...')


class BlaBla(Shell):
    def __init__(self, processor: IProcessor):
        super().__init__(processor)

    def process(self):
        print('Бла бла до...')
        self._processor.process()
        print('Бла бла после...')


if __name__ == '__main__':
    transmitter: IProcessor = Transmitter('42')
    transmitter.process()
    print()

    coder: Shell = SlimBobCoder(transmitter)
    coder.process()
    print()

    bla: Shell = BlaBla(transmitter)
    bla.process()
    print()
