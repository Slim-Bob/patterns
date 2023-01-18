# Пример структурного шаблона проектирования программ «Мост». Он используется в проектировании программного
# обеспечения, разделяя абстракцию и реализацию так, чтобы они могли изменяться независимо.
# Шаблон «Мост» использует инкапсуляцию, агрегирование и может использовать наследование для того, чтобы
# разделить ответственность между классами.

from __future__ import annotations
from abc import ABCMeta, abstractmethod


class IDataReader(metaclass=ABCMeta):
    @abstractmethod
    def read(self):
        pass


class DataBaseReader(IDataReader):
    def read(self):
        print('Данные из БД')


class FileReader(IDataReader):
    def read(self):
        print('Данные из файла')


class Sender(metaclass=ABCMeta):
    def __init__(self, data_reader: IDataReader):
        self.reader: IDataReader = data_reader

    def set_data_reader(self, data_reader: IDataReader):
        self.reader: IDataReader = data_reader

    @abstractmethod
    def send(self):
        pass


class EmailSender(Sender):
    def __init__(self, data_reader: IDataReader):
        super().__init__(data_reader)

    def send(self):
        self.reader.read()
        print('отправлен файл при помощи Email')


class TelegramBotSender(Sender):
    def __init__(self, data_reader: IDataReader):
        super().__init__(data_reader)

    def send(self):
        self.reader.read()
        print('отправлен файл при помощи Telegram Bot')


if __name__ == '__main__':
    sender: Sender = EmailSender(DataBaseReader())
    sender.send()

    sender.set_data_reader(FileReader())
    sender.send()

    sender = TelegramBotSender(DataBaseReader())
    sender.send()
